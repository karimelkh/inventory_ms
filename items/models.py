from django.db import models
from products.models import Product
from suppliers.models import Supplier
from storagesites.models import Site


class Item(models.Model):
    CURRENCIES = [
        ("MAD", "Moroccan Dirham"),
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
        ("CAD", "Canadian Dollar"),
        ("JPY", "Japanese Yen"),
        ("AUD", "Australian Dollar"),
        ("CNY", "Chinese Yuan"),
        ("INR", "Indian Rupee"),
        ("CHF", "Swiss Franc"),
    ]
    id = models.CharField(max_length=50, primary_key=True)
    ttl = models.CharField(max_length=100, blank=False, null=False, unique=True)
    desc = models.CharField(max_length=200)
    qty = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=100, choices=CURRENCIES, default="MAD")
    img = models.ImageField(upload_to="imgs/", null=True, blank=True)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    suppl = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.ttl
