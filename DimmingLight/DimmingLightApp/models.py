from __future__ import unicode_literals
from django.db import models

# Create your models here.
import django
from django import utils

class Dim_Esps(models.Model):

  Modes      = models.CharField(max_length=255, primary_key=True)
  Esps         =  models.CharField(max_length=1000, null=True)
  Time        =  models.CharField(max_length=1000,null=True)
  Light_dim   =  models.CharField(max_length=1000,null=True)
  ChangeDate  =  models.DateTimeField(default=django.utils.timezone.now, blank=True)
  
  class Meta:
      db_table = "Dim_Esps"






