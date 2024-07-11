from django.db import models
from main.models import Supplier, Category, Location

class Item(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_title = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=200)
    stock = models.IntegerField()
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    suppl = models.ForeignKey( Supplier, on_delete=models.CASCADE )
    cat = models.ForeignKey( Category, on_delete=models.CASCADE )
    locat = models.ForeignKey( Location, on_delete=models.CASCADE )
