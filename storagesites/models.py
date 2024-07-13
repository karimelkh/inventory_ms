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
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100)
    site_type = models.CharField(max_length=50, choices=SITE_TYPES)
    site_img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    site_addr = models.CharField(max_length=200)
    site_phone = models.CharField(max_length=12)

    # site_email = models.EmailField(max_length=100)
    # site_capacity = models.
    # site_resp
    # site_man = models.
    # is_active

    def __str__(self):
        return self.site_name
