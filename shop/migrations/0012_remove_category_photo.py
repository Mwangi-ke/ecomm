# Generated by Django 4.2 on 2024-06-19 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_product_inventory_product_in_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
    ]