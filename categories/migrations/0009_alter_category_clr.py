# Generated by Django 5.0.6 on 2024-08-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0008_rename_cat_clr_category_clr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='clr',
            field=models.CharField(choices=[('Red', 'red'), ('Green', 'green'), ('Slate', 'slate'), ('Blue', 'blue'), ('gray', 'gray'), ('Orange', 'orange'), ('Amber', 'amber'), ('Yellow', 'yellow'), ('Lime', 'lime'), ('Emerald', 'emerald'), ('Teal', 'teal'), ('Cyan', 'cyan'), ('Sky', 'sky'), ('Indigo', 'indigo'), ('Violet', 'violet'), ('Purple', 'purple'), ('Pink', 'pink'), ('Rose', 'rose')], max_length=20),
        ),
    ]
