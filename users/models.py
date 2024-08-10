from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    ROLES = [
        ("admin", "Admin"),
        ("staff", "Staff"),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default="staff")
    email = models.EmailField(unique=True)
    gsm = models.CharField(max_length=15, blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
