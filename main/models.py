from django.db import models

class Category(models.Model):
    id_cat = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="def_cat")

    def __str__(self):
        return self.name


class Location(models.Model):
    id_locat = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="def_locat")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    id_suppl = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="def_suppl")

    def __str__(self):
        return self.name
