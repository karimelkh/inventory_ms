# Generated by Django 5.0.6 on 2024-07-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='suppl_desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='suppl_name',
            field=models.CharField(max_length=100),
        ),
    ]
