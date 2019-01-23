from __future__ import unicode_literals
from django.db import models

# Create your models here.
import django
from django import utils
# Create your models here.

#def get_localtimestamp():
#    return django.utils.timezone.now()

class Power_Voltage(models.Model):

  Power_Id    = models.CharField(max_length=50, primary_key=True)
  Power_Voltage     = models.IntegerField() 
  ChangeBy     = models.CharField(max_length=50,null=True) 
  ChangeDate = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  
  
  class Meta:
      db_table = "Power_Voltage"

class Power_Voltage_History(models.Model):

  ActivityId = models.AutoField(primary_key=True)
  Power_Id    = models.CharField(max_length=50)
  Power_Voltage     = models.IntegerField()
  ChangeDate = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  ChangeBy     = models.CharField(max_length=50,null=True)
  class Meta:
      db_table = "Power_Voltage_History"



