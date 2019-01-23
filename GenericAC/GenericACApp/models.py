from __future__ import unicode_literals
from django.db import models
import django
from django import utils
# Create your models here.


class AC_Clients(models.Model):

  ClientId         = models.AutoField(primary_key=True)
  ClientName       = models.CharField(max_length=50,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
      db_table = "AC_Clients"

class AC_Images(models.Model):

  ImgId            = models.AutoField(primary_key=True)
  #Image           = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
  Image            = models.FileField(blank=False, null=False)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
      db_table = "AC_Images"

class AC_Admin(models.Model):

  AdminId          = models.AutoField(primary_key=True)
  AdminDesc        = models.CharField(max_length=50,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  class Meta:
      db_table = "AC_Admin"

class AC_Users(models.Model):
   
  UserId                = models.AutoField(primary_key=True)
  Username              = models.CharField(max_length=50,unique=True)
  Password              = models.CharField(max_length=50,null=True)
  TransPass             = models.CharField(max_length=50,null=True)
  Role                  = models.ForeignKey('AC_Admin',db_column='Role',on_delete=models.CASCADE,default=1)
  ClientId		= models.ForeignKey('AC_Clients',db_column='ClientId',on_delete=models.CASCADE,default=1)
  ImgId                 = models.ForeignKey('AC_Images',db_column='ImgId',on_delete=models.CASCADE,default=1)
  Version		= models.IntegerField(blank=True, null=True,default=1)
  ChangeBy              = models.CharField(max_length=50,null=True)
  StatusActive          = models.BooleanField(default=True)
  ChangeDate            = models.DateTimeField(default=django.utils.timezone.now, blank=True)
  

  class Meta:
      db_table = "AC_Users"
      

class AC_City(models.Model):

  CityId            = models.AutoField(primary_key=True)
  CityDesc          = models.CharField(max_length=50,null=True)
  setTemp           = models.IntegerField(blank=True, null=True)
  ChangeBy          = models.CharField(max_length=50,null=True)
  StatusActive      = models.BooleanField(default=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_City"


class AC_Premise(models.Model):

  PremiseId            = models.AutoField(primary_key=True)
  CityId               = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  PremiseDesc          = models.CharField(max_length=50,null=True)
  setTemp              = models.IntegerField(blank=True, null=True)
  ChangeBy             = models.CharField(max_length=50,null=True)
  StatusActive         = models.BooleanField(default=True)
  ChangeDate           = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Premise"


class AC_Floors(models.Model):

  FloorId          = models.AutoField(primary_key=True)
  FloorDesc        = models.CharField(max_length=50,null=True)
  PremiseId        = models.ForeignKey('AC_Premise',db_column='PremiseId',on_delete=models.CASCADE)
  CityId           = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  ChangeBy         = models.CharField(max_length=50,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Floors"
class AC_Rooms(models.Model):

  RoomId           = models.AutoField(primary_key=True)
  RoomDesc         = models.CharField(max_length=50,null=True)
  FloorId          = models.ForeignKey('AC_Floors',db_column='FloorId',on_delete=models.CASCADE)
  PremiseId        = models.ForeignKey('AC_Premise',db_column='PremiseId',on_delete=models.CASCADE)
  CityId           = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  ChangeBy         = models.CharField(max_length=50,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Rooms"


#{"macid":"30AEA4899FD0","Fan":"1","Status":"0","setTemp":"40","I":"1.1","V":"891","P":"0.3","AVGP":"0.3","ME":"1"}
#{"macid":"3C71BF104EA0","temp":"29","motion":"17269"}

class AC_Input_Units(models.Model):
   
  IpId           = models.AutoField(primary_key=True)
  IpMacid        = models.CharField(max_length=50,null=True)
  IpName         = models.CharField(max_length=50,null=True)
  Abrivation     = models.CharField(max_length=50,null=True)
  FloorId        = models.ForeignKey('AC_Floors',db_column='FloorId',on_delete=models.CASCADE)
  PremiseId      = models.ForeignKey('AC_Premise',db_column='PremiseId',on_delete=models.CASCADE)
  CityId         = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  RoomId         = models.ForeignKey('AC_Rooms',db_column='RoomId',on_delete=models.CASCADE)
  UnitId         = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE)
  Temp	         = models.FloatField(blank=True, null=True)
  Motion         = models.IntegerField(blank=True, null=True)
  ChangeBy       = models.CharField(max_length=50,null=True)
  StatusActive   = models.BooleanField(default=True)
  ChangeDate     = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Input_Units"

class AC_Input_History(models.Model):

  IHId           = models.AutoField(primary_key=True)
  IpMacid        = models.CharField(max_length=50,null=True)
  IpName         = models.CharField(max_length=50,null=True)
  Abrivation     = models.CharField(max_length=50,null=True)
  IpId           = models.ForeignKey('AC_Input_Units',db_column='IpId',on_delete=models.CASCADE)
  UnitId         = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE,default=1)
  Temp           = models.FloatField(blank=True, null=True)
  Motion         = models.IntegerField(blank=True, null=True)
  ChangeBy       = models.CharField(max_length=50,null=True)
  ChangeDate     = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Input_History"
      indexes = [
            models.Index(
                fields=['ChangeDate'],
                name='ChangeDate_idx',
            ),
            models.Index(
                fields=['UnitId'],
                name='UnitId_idx',
            ),
            
        ]

class AC_Operate_Units(models.Model):

  OpId              = models.AutoField(primary_key=True)
  OpMacid           = models.CharField(max_length=50,null=True)
  OpName            = models.CharField(max_length=50,null=True)
  Abrivation        = models.CharField(max_length=50,null=True)
  FloorId           = models.ForeignKey('AC_Floors',db_column='FloorId',on_delete=models.CASCADE)
  PremiseId         = models.ForeignKey('AC_Premise',db_column='PremiseId',on_delete=models.CASCADE)
  CityId            = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  RoomId            = models.ForeignKey('AC_Rooms',db_column='RoomId',on_delete=models.CASCADE)
  UnitId            = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE)
  Fan               = models.CharField(max_length=50,null=True)
  Status            = models.CharField(max_length=50,null=True)
  setTemp           = models.IntegerField(blank=True, null=True)
  Current           = models.FloatField(blank=True, null=True)
  Voltage           = models.FloatField(blank=True, null=True)
  Power             = models.FloatField(blank=True, null=True)
  MotionE           = models.IntegerField(blank=True, null=True)
  ChangeBy          = models.CharField(max_length=50,null=True)
  StatusActive      = models.BooleanField(default=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Operate_Units"

class AC_Operate_History(models.Model):

  OHId              = models.AutoField(primary_key=True)
  OpMacid           = models.CharField(max_length=50,null=True)
  OpName            = models.CharField(max_length=50,null=True)
  Abrivation        = models.CharField(max_length=50,null=True)
  OpId              = models.ForeignKey('AC_Operate_Units',db_column='OpId',on_delete=models.CASCADE)
  UnitId            = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE,default=1)
  Fan               = models.CharField(max_length=50,null=True)
  Status            = models.CharField(max_length=50,null=True)
  setTemp           = models.IntegerField(blank=True, null=True)
  Current           = models.FloatField(blank=True, null=True)
  Voltage           = models.FloatField(blank=True, null=True)
  Power             = models.FloatField(blank=True, null=True)
  MotionE           = models.IntegerField(blank=True, null=True)
  ChangeBy          = models.CharField(max_length=50,null=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Operate_History"
      indexes = [
            models.Index(
                fields=['ChangeDate'],
                name='ChangeDate_idx',
            ),
            models.Index(
                fields=['UnitId'],
                name='UnitId_idx',
            ),
        ]

class AC_Power_Units(models.Model):

  PId              = models.AutoField(primary_key=True)
  PMacid           = models.CharField(max_length=50,null=True)
  PName            = models.CharField(max_length=50,null=True)
  Abrivation        = models.CharField(max_length=50,null=True)
  FloorId           = models.ForeignKey('AC_Floors',db_column='FloorId',on_delete=models.CASCADE)
  PremiseId         = models.ForeignKey('AC_Premise',db_column='PremiseId',on_delete=models.CASCADE)
  CityId            = models.ForeignKey('AC_City',db_column='CityId',on_delete=models.CASCADE)
  RoomId            = models.ForeignKey('AC_Rooms',db_column='RoomId',on_delete=models.CASCADE)
  UnitId            = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE)
  Current           = models.FloatField(blank=True, null=True)
  Voltage           = models.FloatField(blank=True, null=True)
  Power             = models.FloatField(blank=True, null=True)
  ChangeBy          = models.CharField(max_length=50,null=True)
  StatusActive      = models.BooleanField(default=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Power_Units"


class AC_Power_History(models.Model):

  PHId              = models.AutoField(primary_key=True)
  PMacid           = models.CharField(max_length=50,null=True)
  PName            = models.CharField(max_length=50,null=True)
  Abrivation        = models.CharField(max_length=50,null=True)
  PId               = models.ForeignKey('AC_Power_Units',db_column='PId',on_delete=models.CASCADE)
  UnitId         = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE,default=1)
  Current           = models.FloatField(blank=True, null=True)
  Voltage           = models.FloatField(blank=True, null=True)
  Power             = models.FloatField(blank=True, null=True)
  ChangeBy          = models.CharField(max_length=50,null=True)
  ChangeDate        = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Power_History"
      indexes = [
            models.Index(
                fields=['ChangeDate'],
                name='ChangeDate_idx',
            ),
            models.Index(
                fields=['UnitId'],
                name='UnitId_idx',
            ),
        ]
class AC_Units(models.Model):

  UnitId           = models.AutoField(primary_key=True)
  UnitDesc         = models.CharField(max_length=50,null=True)
  ChangeBy         = models.CharField(max_length=50,null=True)
  StatusActive     = models.BooleanField(default=True)
  ChangeDate       = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Units"

class AC_Saved_Units(models.Model):

  SUId           = models.AutoField(primary_key=True)
  Saved          = models.FloatField(blank=True, null=True)
  UnitId         = models.ForeignKey('AC_Units',db_column='UnitId',on_delete=models.CASCADE)
  ChangeBy       = models.CharField(max_length=50,null=True,default='jts_admin')
  StatusActive   = models.BooleanField(default=True)
  ChangeDate     = models.DateTimeField(default=django.utils.timezone.now, blank=True)

  class Meta:
      db_table = "AC_Saved_Units"

