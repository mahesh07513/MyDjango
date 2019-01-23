from __future__ import unicode_literals
from django.db import models
import django
from django import utils

# Create your models here.
class DtD_Users(models.Model):

  Username           = models.CharField(max_length=125,primary_key=True)
  Password           = models.CharField(max_length=255,null=True)
  Address            = models.TextField(null=True, blank=True)
  Company            = models.CharField(max_length=255,null=True)
  Mobile             = models.CharField(max_length=50,null=True)
  Email              = models.CharField(max_length=50,null=True)
  ChangeDate         = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "DtD_Users"

class DtD_Units(models.Model):

  UnitId             = models.AutoField(primary_key=True)
  UnitDesc           = models.CharField(max_length=125,null=True)
  UnitMac           = models.CharField(max_length=125,null=True)
  Longitude          = models.FloatField(null=True, blank=True, default=None)
  Latitude           = models.FloatField(null=True, blank=True, default=None)
  Operation          = models.CharField(max_length=50,null=True,default='OFF')
  ChangeBy           = models.CharField(max_length=125,null=True)
  ChangeDate         = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "DtD_Units"

class DtD_Unit_Details(models.Model):
  
  UDId               = models.AutoField(primary_key=True)
  UnitId             = models.ForeignKey('DtD_Units',db_column='UnitId',on_delete=models.CASCADE)
  Type               = models.CharField(max_length=125,null=True)
  PosNeg               = models.CharField(max_length=125,null=True)
  Hours               = models.CharField(max_length=125,null=True)
  Mns               = models.CharField(max_length=125,null=True)
  Status               = models.CharField(max_length=125,null=True)
  ChangeBy           = models.CharField(max_length=125,null=True)
  ChangeDate         = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "DtD_Unit_Details"

