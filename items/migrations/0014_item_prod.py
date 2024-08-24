# Generated by Django 5.0.6 on 2024-08-14 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_item_suppl'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='prod',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]
