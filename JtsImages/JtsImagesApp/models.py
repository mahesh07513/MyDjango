from __future__ import unicode_literals
from django.db import models
import django
from django import utils
# Create your models here.

class JTS_Images(models.Model):

  ImgId            = models.AutoField(primary_key=True)
  #Image           = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
  #Image            = models.FileField(blank=False, null=False)
  Image            =  models.CharField(max_length=255,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
      db_table = "JTS_Images"


