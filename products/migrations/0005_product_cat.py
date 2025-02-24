# Generated by Django 5.0.6 on 2024-08-31 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_alter_category_clr'),
        ('products', '0004_rename_art_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
            preserve_default=False,
        ),
    ]
