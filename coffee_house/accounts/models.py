from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.EmailField()
#     age = models.PositiveSmallIntegerField()
#     country = models.CharField(max_length=99)
#     city = models.CharField(max_length=99)
#     sex = models.CharField(max_length=255)


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True)
    age = models.PositiveSmallIntegerField(blank=True, default=0)
    country = models.CharField(max_length=99, blank=True)
    city = models.CharField(max_length=99, blank=True)
    sex = models.CharField(max_length=255, blank=True)
