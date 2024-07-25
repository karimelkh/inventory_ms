from django.db import models


class Category(models.Model):
    COLOR_CHOICES = [
        ("red", "Red"),
        ("green", "Green"),
        ("slate", "Slate"),
        ("blue", "Blue"),
        ("gray", "gray"),
        ("orange", "Orange"),
        ("amber", "Amber"),
        ("yellow", "Yellow"),
        ("lime", "Lime"),
        ("emerald", "Emerald"),
        ("teal", "Teal"),
        ("cyan", "Cyan"),
        ("sky", "Sky"),
        ("indigo", "Indigo"),
        ("violet", "Violet"),
        ("purple", "Purple"),
        ("pink", "Pink"),
        ("rose", "Rose"),
    ]
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    cat_desc = models.CharField(max_length=200)
    cat_clr = models.CharField(max_length=20, choices=COLOR_CHOICES)

    def __str__(self):
        return self.cat_name
