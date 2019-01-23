# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-22 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuskToDawnApp', '0003_auto_20180821_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtd_units',
            name='Ab',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Dw',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Sr',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Ss',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='dtd_units',
            name='Tw',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='dtd_units',
            name='Operation',
            field=models.CharField(default='OFF', max_length=50, null=True),
        ),
    ]
