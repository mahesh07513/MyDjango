from __future__ import unicode_literals
from django.db import models

# Create your models here.
import django
from django import utils
# Create your models here.

#def get_localtimestamp():
#    return django.utils.timezone.now()

class Current_Status(models.Model):

  TowerId    = models.CharField(max_length=50, primary_key=True)
  Status     = models.CharField(max_length=10)
  ChangeDate = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  ChangeBy     = models.CharField(max_length=50,null=True) 
  Operate     = models.CharField(max_length=50,null=True)
  class Meta:
      db_table = "Current_Status"

class Current_Status_History(models.Model):

  ActivityId = models.AutoField(primary_key=True)
  TowerId    = models.CharField(max_length=50)
  Status     = models.CharField(max_length=10)
  ChangeDate = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  ChangeBy     = models.CharField(max_length=50,null=True)
  class Meta:
      db_table = "Current_Status_History"

class Login_Users(models.Model):

  Uname    = models.CharField(max_length=50, primary_key=True)
  Pass     = models.CharField(max_length=50)
  ChangeDate = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  #ChangeBy     = models.CharField(max_length=50,null=True)

  class Meta:
      db_table = "Login_Users"

