# Generated by Django 5.0.6 on 2024-08-19 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_alter_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='prod',
        ),
    ]
