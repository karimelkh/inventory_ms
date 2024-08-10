from django.db import models

class Site(models.Model):
    SITE_TYPES = [
            ("Public", "public"),
            ("Private", "private"),
            ("Smart", "smart"),
            ("Hazmat", "hazmat"),
            ("Cold storage", "cold"),
            ("Distribution Center", "distribution"),
        ]
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=SITE_TYPES)
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    addr = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, unique=True)

    # email = models.EmailField(max_length=100)
    # capacity = models.
    # resp
    # man = models.
    # is_active

    def __str__(self):
        return self.name
