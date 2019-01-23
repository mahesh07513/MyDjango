# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-21 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuskToDawnApp', '0002_dtd_units_unitdesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dtd_units',
            name='Lat',
        ),
        migrations.RemoveField(
            model_name='dtd_units',
            name='Long',
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
