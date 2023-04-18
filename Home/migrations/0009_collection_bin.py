# Generated by Django 4.1.1 on 2023-04-05 05:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_complaintpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_bin',
            fields=[
                ('Bin_id', models.AutoField(primary_key=True, serialize=False)),
                ('Bin_name', models.CharField(max_length=100, unique=True)),
                ('Bin_address1', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Invalid address.', regex='^[\\w\\-\\. ]+$')])),
                ('Bin_address2', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Invalid address.', regex='^[\\w\\-\\. ]+$')])),
                ('Bin_address3', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Invalid address.', regex='^[\\w\\-\\. ]+$')])),
                ('pincode', models.BigIntegerField(validators=[django.core.validators.RegexValidator(message='Invalid pincode.', regex='^[0-9]{6}$')])),
                ('distance_KM', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.RegexValidator(message='Invalid distance.', regex='^\\d+(\\.\\d{1,2})?$')])),
                ('total_time', models.TimeField(default='00:00:00')),
                ('Bin_date', models.DateField()),
                ('Bin_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('Bin_color', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.bin_color', verbose_name='bin_color')),
                ('Bin_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.location', verbose_name='region')),
                ('collections_day', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.scheduleingday', verbose_name='day')),
            ],
        ),
    ]