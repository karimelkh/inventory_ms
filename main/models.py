from django.db import models

class Location(models.Model):
    id_locat = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="def_locat")

    def __str__(self):
        return self.name
