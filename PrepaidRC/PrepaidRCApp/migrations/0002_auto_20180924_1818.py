# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-24 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrepaidRCApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prepaid_cat_fares',
            name='Commercial',
        ),
        migrations.RemoveField(
            model_name='prepaid_cat_fares',
            name='Domestic',
        ),
        migrations.RemoveField(
            model_name='prepaid_cat_fares',
            name='Units',
        ),
        migrations.AddField(
            model_name='prepaid_cat_fares',
            name='CatId',
            field=models.ForeignKey(db_column='CatId', default='', on_delete=django.db.models.deletion.CASCADE, to='PrepaidRCApp.Prepaid_Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prepaid_cat_fares',
            name='U100',
            field=models.FloatField(blank=True, db_column='U_51-100', null=True),
        ),
        migrations.AddField(
            model_name='prepaid_cat_fares',
            name='U50',
            field=models.FloatField(blank=True, db_column='U_0-50', null=True),
        ),
    ]
