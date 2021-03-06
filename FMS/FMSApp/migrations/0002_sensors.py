# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FMSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('Sensor_ID', models.AutoField(primary_key=True, serialize=False)),
                ('IsActive', models.NullBooleanField()),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('LU_ID', models.ForeignKey(db_column='Sensor_Type_LU', on_delete=django.db.models.deletion.CASCADE, to='FMSApp.Lookup')),
            ],
            options={
                'db_table': 'Sensors',
            },
        ),
    ]
