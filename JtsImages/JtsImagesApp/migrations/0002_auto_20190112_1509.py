# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-12 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JtsImagesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jts_images',
            name='Image',
            field=models.CharField(max_length=50, null=True),
        ),
    ]