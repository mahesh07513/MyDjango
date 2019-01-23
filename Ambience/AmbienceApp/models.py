from __future__ import unicode_literals
from django.db import models

# Create your models here.
import django
from django import utils
# Create your models here.

class Light_Users(models.Model):
   UserId       = models.AutoField(primary_key=True)
   Username     = models.CharField(max_length=125)
   Password     = models.CharField(max_length=125)
   Name         = models.CharField(max_length=125,null=True)
   Email	= models.CharField(max_length=50,null=True)
   Mobile       = models.CharField(max_length=50,null=True)
   OrgTypeId    = models.ForeignKey('Light_Org_Types',db_column='OrgTypeId',on_delete=models.CASCADE)
   Country      = models.CharField(max_length=125,null=True)
   Address      = models.CharField(max_length=125,null=True)
   OrgId        = models.ForeignKey('Light_Orgs',db_column='OrgId',on_delete=models.CASCADE)
   ChangeDate   = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Users"

class Light_Org_Types(models.Model):
   OrgTypeId       = models.AutoField(primary_key=True)
   OrgTypeDesc     = models.CharField(max_length=125)
   ChangeBy        = models.CharField(max_length=125,null=True)
   ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Org_Types"

class Light_Orgs(models.Model):
   OrgId       = models.AutoField(primary_key=True)
   OrgDesc     = models.CharField(max_length=125)
   ChangeBy    = models.CharField(max_length=125,null=True)
   ChangeDate  = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Orgs"

class Light_Premises(models.Model):
   PremiseId        = models.AutoField(primary_key=True)
   PremiseDesc     = models.CharField(max_length=125)
   OrgId           = models.ForeignKey('Light_Orgs',db_column='OrgId',on_delete=models.CASCADE)
   ChangeBy        = models.CharField(max_length=125,null=True)
   ChangeDate      = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Premises"

class Light_Spaces(models.Model):
   SpaceId       = models.AutoField(primary_key=True)
   SpaceDesc     = models.CharField(max_length=125)
   SpaceSize     = models.CharField(max_length=125,null=True)
   PremiseId     = models.ForeignKey('Light_Premises',db_column='PremiseId',on_delete=models.CASCADE)
   ChangeBy      = models.CharField(max_length=125,null=True)
   ChangeDate    = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Spaces"

class Light_Spaces_Nodes(models.Model):
   NodeId       = models.AutoField(primary_key=True)
   NodeDesc     = models.CharField(max_length=125)
   NodeSize     = models.CharField(max_length=125,null=True)
   SpaceId      = models.ForeignKey('Light_Spaces',db_column='SpaceId',on_delete=models.CASCADE)
   ChangeBy      = models.CharField(max_length=125,null=True)
   ChangeDate    = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Spaces_Nodes"

'''
class Light_Routers(models.Model):
   RouterId        = models.AutoField(primary_key=True)
   RouterSSID     = models.CharField(max_length=125)
   Password        = models.CharField(max_length=125)
   PremiseId       = models.ForeignKey('Light_Premises',db_column='PremiseId',on_delete=models.CASCADE)
   ChangeBy        = models.CharField(max_length=125,null=True)
   ChangeDate      = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Light_Routers"


class Light_Premisis_Lights(models.Model):
   ActivityId      = models.AutoField(primary_key=True)
   Light_Bot       = models.CharField(max_length=255,null=True)
   PremiseId       = models.ForeignKey('Light_Premises',db_column='PremiseId',on_delete=models.CASCADE)
   RouterId        = models.ForeignKey('Light_Routers',db_column='RouterId',on_delete=models.CASCADE)
   ChangeBy        = models.CharField(max_length=125,null=True)
   ChangeDate      = models.DateTimeField(default=django.utils.timezone.now, blank=True)

   class Meta:
      db_table = "Light_Premisis_Lights"

class Light_Status(models.Model):
  StatusId         = models.AutoField(primary_key=True)
  esp_id           = models.CharField(max_length=50, primary_key=True)
  mobile_id        = models.CharField(max_length=255,null=True)
  cct              = models.CharField(max_length=50,null=True)
  light_intencity1 = models.CharField(max_length=50,null=True)
  light_intencity2 = models.CharField(max_length=50,null=True)
  light_intencity3 = models.CharField(max_length=50,null=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "Light_Status"


'''





