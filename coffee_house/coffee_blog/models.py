from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order model"""
    user_surname = models.CharField(max_length=250, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)