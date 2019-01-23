# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-24 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GrowBoxApp', '0002_gb_growdata_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='BLE_Data',
            fields=[
                ('BId', models.AutoField(primary_key=True, serialize=False)),
                ('Macid', models.CharField(max_length=50, null=True)),
                ('Temp', models.FloatField(blank=True, null=True)),
                ('Rssi', models.FloatField(blank=True, null=True)),
                ('ChangeBy', models.CharField(max_length=50, null=True)),
                ('StatusActive', models.BooleanField(default=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'BLE_Data',
            },
        ),
        migrations.CreateModel(
            name='BLE_Data_History',
            fields=[
                ('BHId', models.AutoField(primary_key=True, serialize=False)),
                ('Macid', models.CharField(max_length=50, null=True)),
                ('Temp', models.FloatField(blank=True, null=True)),
                ('Rssi', models.FloatField(blank=True, null=True)),
                ('ChangeBy', models.CharField(max_length=50, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('BId', models.ForeignKey(db_column='BId', default=1, on_delete=django.db.models.deletion.CASCADE, to='GrowBoxApp.BLE_Data')),
            ],
            options={
                'db_table': 'BLE_Data_History',
            },
        ),
    ]