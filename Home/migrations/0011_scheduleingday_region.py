# Generated by Django 4.1.1 on 2022-11-20 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_workupdation'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleingday',
            name='region',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.location', verbose_name='region'),
        ),
    ]