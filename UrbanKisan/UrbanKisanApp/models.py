from __future__ import unicode_literals
from django.db import models
import django
from django import utils
# Create your models here.
class UK_Unit_Params(models.Model):
   
  UnitId            = models.AutoField(primary_key=True)
  MacId             = models.CharField(max_length=125,unique=True)
  Temp 		    = models.IntegerField(max_length=125,null=True)
  WaterLevel        = models.IntegerField(blank=True, null=True)
  Ph                = models.FloatField(blank=True, null=True)
  EC                = models.FloatField(blank=True, null=True)
  Ppm 		    = models.IntegerField(blank=True, null=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "UK_Unit_Params"


class UK_Unit_History(models.Model):

  UHId              = models.AutoField(primary_key=True)
  UnitId            = models.ForeignKey('UK_Unit_Params',db_column='UnitId',on_delete=models.CASCADE)
  MacId             = models.CharField(max_length=125,null=True)
  Temp              = models.IntegerField(max_length=125,null=True)
  WaterLevel        = models.IntegerField(blank=True, null=True)
  Ph                = models.FloatField(blank=True, null=True)
  EC                = models.FloatField(blank=True, null=True)
  Ppm               = models.IntegerField(blank=True, null=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "UK_Unit_History"
