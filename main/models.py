from django.db import models

class Category(models.Model):
    id_cat = models.AutoField(primary_key=True)

class Location(models.Model):
    id_locat = models.AutoField(primary_key=True)

class Supplier(models.Model):
    id_suppl = models.AutoField(primary_key=True)
