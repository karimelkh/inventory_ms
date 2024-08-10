# Generated by Django 5.0.6 on 2024-08-10 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_remove_item_suppl'),
        ('suppliers', '0011_alter_supplier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='suppl',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier'),
            preserve_default=False,
        ),
    ]
