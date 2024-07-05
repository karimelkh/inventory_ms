from django.db import models

class Category(models.Model):
    id_cat = models.AutoField(primary_key=True)


class Location(models.Model):
    id_locat = models.AutoField(primary_key=True)


class Supplier(models.Model):
    id_suppl = models.AutoField(primary_key=True)


class Product(models.Model):
    PROD_STATS = {
        "": "",
    }
    id_prod = models.AutoField(primary_key=True)
    prod_title = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=200)
    qty_in_stock = models.IntegerField()
#    prod_status = models.CharField(
#        max_length = 2,
#        choices = PROD_STATS,
        # default = '',
#    )
#    prod_img = models.ImageField(upload_tp='')
    suppl = models.ForeignKey( "Supplier", on_delete=models.CASCADE )
    cat = models.ForeignKey( "Category", on_delete=models.CASCADE )
    locat = models.ForeignKey( "Location", on_delete=models.CASCADE )


 
#    class Order(models.Model):
#        def __str__(self):
#            return self.name
# 
# 
#    class Ordered_product(models.Model):
#        def __str__(self):
#            return self.name
