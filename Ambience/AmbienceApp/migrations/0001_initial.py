# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-09 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light_Org_Types',
            fields=[
                ('OrgTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('OrgTypeDesc', models.CharField(max_length=125)),
                ('ChangeBy', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Light_Org_Types',
            },
        ),
        migrations.CreateModel(
            name='Light_Orgs',
            fields=[
                ('OrgId', models.AutoField(primary_key=True, serialize=False)),
                ('OrgDesc', models.CharField(max_length=125)),
                ('ChangeBy', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Light_Orgs',
            },
        ),
        migrations.CreateModel(
            name='Light_Premises',
            fields=[
                ('PremiseId', models.AutoField(primary_key=True, serialize=False)),
                ('PremiseDesc', models.CharField(max_length=125)),
                ('ChangeBy', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('OrgId', models.ForeignKey(db_column='OrgId', on_delete=django.db.models.deletion.CASCADE, to='AmbienceApp.Light_Orgs')),
            ],
            options={
                'db_table': 'Light_Premises',
            },
        ),
        migrations.CreateModel(
            name='Light_Spaces',
            fields=[
                ('SpaceId', models.AutoField(primary_key=True, serialize=False)),
                ('SpaceDesc', models.CharField(max_length=125)),
                ('SpaceSize', models.CharField(max_length=125, null=True)),
                ('ChangeBy', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('PremiseId', models.ForeignKey(db_column='PremiseId', on_delete=django.db.models.deletion.CASCADE, to='AmbienceApp.Light_Premises')),
            ],
            options={
                'db_table': 'Light_Spaces',
            },
        ),
        migrations.CreateModel(
            name='Light_Spaces_Nodes',
            fields=[
                ('NodeId', models.AutoField(primary_key=True, serialize=False)),
                ('NodeDesc', models.CharField(max_length=125)),
                ('NodeSize', models.CharField(max_length=125, null=True)),
                ('ChangeBy', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('SpaceId', models.ForeignKey(db_column='SpaceId', on_delete=django.db.models.deletion.CASCADE, to='AmbienceApp.Light_Spaces')),
            ],
            options={
                'db_table': 'Light_Spaces_Nodes',
            },
        ),
        migrations.CreateModel(
            name='Light_Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=125)),
                ('Password', models.CharField(max_length=125)),
                ('Name', models.CharField(max_length=125, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('Mobile', models.CharField(max_length=50, null=True)),
                ('Country', models.CharField(max_length=125, null=True)),
                ('Address', models.CharField(max_length=125, null=True)),
                ('ChangeDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('OrgId', models.ForeignKey(db_column='OrgId', on_delete=django.db.models.deletion.CASCADE, to='AmbienceApp.Light_Orgs')),
                ('OrgTypeId', models.ForeignKey(db_column='OrgTypeId', on_delete=django.db.models.deletion.CASCADE, to='AmbienceApp.Light_Org_Types')),
            ],
            options={
                'db_table': 'Light_Users',
            },
        ),
    ]