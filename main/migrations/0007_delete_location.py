# Generated by Django 5.0.6 on 2024-07-13 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_locat'),
        ('main', '0006_delete_supplier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]
