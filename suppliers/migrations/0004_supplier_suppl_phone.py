# Generated by Django 5.0.6 on 2024-07-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_supplier_suppl_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='suppl_phone',
            field=models.CharField(default='999999999999', max_length=12),
        ),
    ]
