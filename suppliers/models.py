from django.db import models


class Supplier(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)
    addr = models.CharField(max_length=200)
    site = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)

    def __str__(self):
        return self.name
