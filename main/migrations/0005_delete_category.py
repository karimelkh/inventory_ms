# Generated by Django 5.0.6 on 2024-07-12 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_cat'),
        ('main', '0004_category_name_location_name_supplier_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
