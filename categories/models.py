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

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    desc = models.CharField(max_length=200)
    clr = models.CharField(max_length=20, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name
