# Generated by Django 4.2 on 2024-06-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_audiosystem_subcategory_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default='New', max_length=50),
        ),
    ]
