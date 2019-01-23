from __future__ import unicode_literals
from django.db import models

# Create your models here.
import django
from django import utils

class Asset_Rooms(models.Model):
  
  Room_id        =  models.CharField(max_length=255,primary_key=True) 
  Room_desc      =  models.CharField(max_length=255)
  Change_Date    =  models.DateTimeField(default=django.utils.timezone.now, blank=True)  
  class Meta:
    db_table = "Asset_Rooms"

class Asset_SSID(models.Model):
  Ssid          =  models.CharField(max_length=255,primary_key=True)
  Ssid_tag      =  models.CharField(max_length=255,null=True)
  Room_id       =  models.ForeignKey('Asset_Rooms',db_column='Room_id',on_delete=models.CASCADE)
  #Str_ssid     =  models.CharField(max_length=10,null=True)
  Change_Date   =  models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
    db_table = "Asset_SSID"

class Asset_Ssid_Str(models.Model):
  Ssid          =  models.ForeignKey('Asset_SSID',db_column='Ssid',on_delete=models.CASCADE)
  Room_id       =  models.ForeignKey('Asset_Rooms',db_column='Room_id',on_delete=models.CASCADE)
  Str_ssid     =  models.CharField(max_length=10,null=True)
  Change_Date   =  models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
    db_table = "Asset_Ssid_Str"


