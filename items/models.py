from django.db import models
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site


class Item(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ttl = models.CharField(max_length=100, blank=False, null=False, unique=True)
    desc = models.CharField(max_length=200)
    qty = models.IntegerField(blank=False, null=False)
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    suppl = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.ttl
