# Generated by Django 4.1.1 on 2023-04-19 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_bins_bin_address1_alter_bins_bin_address2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bins',
            name='Bin_address1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bins',
            name='Bin_address2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bins',
            name='Bin_address3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bins',
            name='Bin_date',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='bins',
            name='Bin_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bins',
            name='Bin_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bins',
            name='distance_KM',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bins',
            name='pincode',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bins',
            name='total_time',
            field=models.TimeField(default=0),
        ),
    ]
