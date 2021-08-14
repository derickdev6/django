# Django
from django.db import models


class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_premium = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
