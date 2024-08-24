from django.db import models

class SiteType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

# TODO: add these fields
class Site(models.Model):
    # SITE_TYPES = [
    #         ("Public", "Public"),
    #         ("Private", "Private"),
    #         ("Smart", "Smart"),
    #         ("Hazmat", "Hazmat"),
    #         ("Cold storage", "Cold storage"),
    #         ("Distribution Center", "Distribution Center"),
    #     ]
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # type = models.CharField(max_length=50, choices=SITE_TYPES)
    # TODO: change SET_NULL to DO_NOTHING
    type = models.ForeignKey(SiteType, on_delete=models.SET_NULL, null=True)
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
