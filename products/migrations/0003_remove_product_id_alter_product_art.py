# Generated by Django 5.0.6 on 2024-08-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_art_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='art',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
