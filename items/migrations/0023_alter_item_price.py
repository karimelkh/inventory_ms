# Generated by Django 5.0.6 on 2024-08-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
