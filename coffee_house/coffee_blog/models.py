from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img')
    text = models.TextField()
    short_description = models.CharField(max_length=250, default='')
    url = models.SlugField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.pk})


class Order(models.Model):
    user_name = models.CharField(max_length=250)
    user_surname = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveIntegerField()

