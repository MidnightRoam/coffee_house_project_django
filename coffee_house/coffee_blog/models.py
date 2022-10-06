from datetime import datetime

from django.db import models
from django.urls import reverse

from accounts.models import User


class Blog(models.Model):
    """Blog model"""
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img')
    text = models.TextField()
    short_description = models.CharField(max_length=250, default='')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"blog_slug": self.slug})


class ProductCategory(models.Model):
    """Product category model"""
    name = models.CharField("Category", max_length=64)
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=255, default='')
    short_description = models.CharField(max_length=64, default='')
    image = models.ImageField(upload_to='product_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    created_timestamp = models.DateTimeField(default=datetime.now())
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name
