from django.db import models

class Supplier(models.Model):
    suppl_id = models.AutoField(primary_key=True)
    suppl_name = models.CharField(max_length=100)
    suppl_desc = models.CharField(max_length=200, null=True, blank=True)
    suppl_email = models.EmailField()
    suppl_addr = models.CharField(max_length=200)
    suppl_site = models.URLField(null=True, blank=True)
    suppl_phone = models.CharField(max_length=12)
    # suppl_phone = models.CharField(max_length=12, default="999999999999")
    is_active = models.BooleanField(default=True)
    suppl_img = models.ImageField(upload_to="imgs/", null=True, blank=True)

    def __str__(self):
        return self.suppl_name
