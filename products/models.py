from django.db import models

# TODO: mv cat here
class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ttl = models.CharField(max_length=100, blank=False, null=False, unique=True)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)

    def __str__(self):
        return self.ttl
