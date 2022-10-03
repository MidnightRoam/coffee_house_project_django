from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model"""
    image = models.ImageField(upload_to="users_images", blank=True)
    age = models.PositiveSmallIntegerField(blank=True, default=0)
    country = models.CharField(max_length=99, blank=True)
    city = models.CharField(max_length=99, blank=True)
    sex = models.CharField(max_length=255, blank=True)
