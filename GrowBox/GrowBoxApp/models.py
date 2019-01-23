from __future__ import unicode_literals
from django.db import models
import django
from django import utils
# Create your models here.

class GB_GrowData(models.Model):

  GBId                  = models.AutoField(primary_key=True)
  Macid                 = models.CharField(max_length=50,null=True)
  Chamber1Temp          = models.FloatField(blank=True, null=True)
  Chamber1Humi          = models.FloatField(blank=True, null=True)
  Chamber2Temp          = models.FloatField(blank=True, null=True)
  Chamber2Humi          = models.FloatField(blank=True, null=True)
  Chamber3Temp          = models.FloatField(blank=True, null=True)
  Chamber3Humi          = models.FloatField(blank=True, null=True)
  ChillerTemp           = models.FloatField(blank=True, null=True)
  ChangeBy              = models.CharField(max_length=50,null=True)
  StatusActive          = models.BooleanField(default=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "GB_GrowData"

class GB_GrowData_History(models.Model):

  GBHId                 = models.AutoField(primary_key=True)
  GBId	          	= models.ForeignKey('GB_GrowData',db_column='GBId',on_delete=models.CASCADE,default=1)
  Macid                 = models.CharField(max_length=50,null=True)
  Chamber1Temp          = models.FloatField(blank=True, null=True)
  Chamber1Humi          = models.FloatField(blank=True, null=True)
  Chamber2Temp          = models.FloatField(blank=True, null=True)
  Chamber2Humi          = models.FloatField(blank=True, null=True)
  Chamber3Temp          = models.FloatField(blank=True, null=True)
  Chamber3Humi          = models.FloatField(blank=True, null=True)
  ChillerTemp           = models.FloatField(blank=True, null=True)
  ChangeBy              = models.CharField(max_length=50,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "GB_GrowData_History"


class BLE_Data(models.Model):

  BId                   = models.AutoField(primary_key=True)
  Macid                 = models.CharField(max_length=50,null=True)
  Temp                  = models.FloatField(blank=True, null=True)
  Rssi                  = models.FloatField(blank=True, null=True)
  ChangeBy              = models.CharField(max_length=50,null=True)
  StatusActive          = models.BooleanField(default=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "BLE_Data"

class BLE_Data_History(models.Model):

  BHId                  = models.AutoField(primary_key=True)
  BId                   = models.ForeignKey('BLE_Data',db_column='BId',on_delete=models.CASCADE,default=1)
  Macid                 = models.CharField(max_length=50,null=True)
  Temp                  = models.FloatField(blank=True, null=True)
  Rssi                  = models.FloatField(blank=True, null=True)
  ChangeBy              = models.CharField(max_length=50,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "BLE_Data_History"

