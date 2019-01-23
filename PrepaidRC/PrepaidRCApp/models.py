from __future__ import unicode_literals
from django.db import models
import django
from django import utils
# Create your models here.

class Prepaid_Users(models.Model):
   
  UserId                = models.AutoField(primary_key=True)
  Username              = models.CharField(max_length=125,unique=True)
  Password              = models.CharField(max_length=255,null=True)
  Phone                 = models.CharField(max_length=255,null=True)
  Email                 = models.CharField(max_length=255,null=True)
  CatId                = models.ForeignKey('Prepaid_Category',db_column='CatId',on_delete=models.CASCADE)
  ChangeBy              = models.CharField(max_length=255,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Users"

class Prepaid_Meters(models.Model):

  MeterId               = models.AutoField(primary_key=True)
  MacID                 = models.CharField(max_length=125,unique=True)
  UserId               = models.ForeignKey('Prepaid_Users',db_column='UserId',on_delete=models.CASCADE)
  CatId                = models.ForeignKey('Prepaid_Category',db_column='CatId',on_delete=models.CASCADE)
  Units                 = models.FloatField(null=True, blank=True) 
  ChangeBy              = models.CharField(max_length=255,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Meters"

class Prepaid_Payment(models.Model):

  TransactionId         = models.AutoField(primary_key=True)
  Paid                  = models.FloatField(blank=True, null=True)
  MeterId               = models.ForeignKey('Prepaid_Meters',db_column='MeterId',on_delete=models.CASCADE)
  UserId               = models.ForeignKey('Prepaid_Users',db_column='UserId',on_delete=models.CASCADE)
  CatId                = models.ForeignKey('Prepaid_Category',db_column='CatId',on_delete=models.CASCADE)
  ChangeBy              = models.CharField(max_length=255,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Payment"


class Prepaid_Usage_History(models.Model):

  MeterIdH              = models.AutoField(primary_key=True)
  MeterId               = models.ForeignKey('Prepaid_Meters',db_column='MeterId',on_delete=models.CASCADE)
  Units                 = models.FloatField(null=True, blank=True)  
  ChangeBy              = models.CharField(max_length=255,null=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Usage_History"

class Prepaid_Category(models.Model):

  CatId               = models.AutoField(primary_key=True)
  CatDesc             = models.CharField(max_length=255,null=True)
  ChangeBy            = models.CharField(max_length=255,null=True)
  ChangeDate          = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Category"

class Prepaid_Cat_Fares(models.Model):

  CatFareId            = models.AutoField(primary_key=True)
  CatId                = models.ForeignKey('Prepaid_Category',db_column='CatId',on_delete=models.CASCADE)
  U50             = models.FloatField(null=True, blank=True,db_column='U0T50') 
  U100           = models.FloatField(null=True, blank=True,db_column='U51T100')
  ChangeDate           = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Prepaid_Cat_Fares"

