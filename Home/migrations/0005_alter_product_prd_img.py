# Generated by Django 4.1.1 on 2023-03-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_product_prd_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prd_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
