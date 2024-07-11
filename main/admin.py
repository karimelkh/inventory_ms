from django.contrib import admin
from .models import Category, Location, Supplier

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Supplier)
