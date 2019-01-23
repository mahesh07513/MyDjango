from __future__ import unicode_literals

from django.db import models
import django
from django import utils
# Create your models here.

class SysLookup(models.Model):

  SLU_ID           = models.AutoField(primary_key=True)
  SysLookup_Desc   = models.CharField(max_length=512,null=True)
  IsActive         = models.NullBooleanField(blank=True,null=True) 
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "SysLookup"

class Lookup(models.Model):

  LU_ID            = models.AutoField(primary_key=True)
  LU_Value         = models.CharField(max_length=512,null=True)
  IsActive         = models.NullBooleanField(blank=True,null=True) 
  SLU_ID           = models.ForeignKey('SysLookup',db_column='Syslookup_ID',on_delete=models.CASCADE)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Lookup"


class Sensors(models.Model):

  Sensor_ID            = models.AutoField(primary_key=True)
  IsActive             = models.NullBooleanField(blank=True,null=True)
  LU_ID                = models.ForeignKey('Lookup',db_column='Sensor_Type_LU',on_delete=models.CASCADE)
  ChangeDate           = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Sensors"


#############payment######################
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):

    def get_failure_url(self):
        return 'http://cld003.jts-prod.in:5911/failure/'

    def get_success_url(self):
        return 'http://cld003.jts-prod.in:5911/success/'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',
                            quantity=2, price=Decimal(1), currency='INR')
