# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-24 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrepaidRCApp', '0002_auto_20180924_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaid_cat_fares',
            name='U100',
            field=models.FloatField(blank=True, db_column='U51100', null=True),
        ),
        migrations.AlterField(
            model_name='prepaid_cat_fares',
            name='U50',
            field=models.FloatField(blank=True, db_column='U050', null=True),
        ),
    ]
