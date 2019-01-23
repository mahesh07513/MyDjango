from __future__ import unicode_literals
from django.shortcuts import render
#from datetime import tzinfo,timedelta
import requests
# Create your views here.
from GenericACApp.models import *
from django.http import HttpResponse
from django.http import JsonResponse
import json
import logging
#from django.core.exceptions import DatabaseError
from django.db.models import *
import urllib2
#from datetime import datetime,timedelta
#import datetime as dt1
import time
#import timedelta
#import datetime
from datetime import datetime
import pytz
import sys
import socket
from django.db.models import Count

from dateutil import rrule
import itertools
import pandas as pd
from pandas import DataFrame
# Create your views here.

'''
##################AddUser###############################
def add_user(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_user: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_user- Unable to Authenticate/add_user... "
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_user:"+ output)
        HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("add_user:input: user="+username)

     #check authentication (temporary, this will need to be implemented)
     is_rec_needed = False
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():
             
        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Add/Modify."}'
        logging.debug("add_user:"+ output)
        return HttpResponse(output)


     try:
     #{
        if((data1.get('Uname') is None) or ((data1.get('Uname') is not  None) and (len(data1['Uname']) <= 0))):
           output_str += ",Uname is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           uname = data1['Uname']

        if((data1.get('Pass') is None) or ((data1.get('Pass') is not  None) and (len(data1['Pass']) <= 0))):
           output_str += ",Pass is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           pass1 = data1['Pass']

        if((data1.get('Role') is None) or ((data1.get('Role') is not  None) and (len(data1['Role']) <= 0))):
           output_str += ",Role is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           role = data1['Role']
  
        #get the status from DB
        AC_usrget = AC_Users.objects.filter(Username=uname,Password=pass1)
        print oyo_usrget       
        if(len(oyo_usrget) > 0):
           output_str = "User Already Exits"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           role1=AC_Admin.objects.get(AdminId=role)
           add_usr_rec=AC_Users(Username=uname,Password=pass1,ChangeBy=username,Role=role1);
           add_usr_rec.save()
           if(add_usr_rec > 0):
             output = '{"error_code":"0", "Response":"Successfully added the User, %s"}' %(uname)
             logging.debug("add_user:"+ output)
             return HttpResponse(output)
           else:
              output = '{"error_code":"3", "error_desc": "Response=Failed to add the user"}'
              logging.debug("add_user:"+ output)
              return HttpResponse(output)
  
           
     #}
     except Exception, e:
     #{
         err_desc = 'add_user:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_user:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the user"}'
         logging.debug("add_user:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_user: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_user:"+ output)
      return HttpResponse(output)



#############################Login###############################
def login(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("login: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "login- Unable to Authenticate/login... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("login:"+ output)
        return HttpResponse(output)
     
     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("login:input: user="+username)
     
     if AC_Users.objects.filter(Username = username,Password=password).exists():
     #{
          print("yes")
          #print(AdminSupp.objects.values('uname'))
          get_role=AC_Users.objects.filter(Username = username,Password=password).only("Role")
     	  role=get_role[0].Role.AdminDesc          
          print "",get_role[0].Role.AdminId
          print "",get_role[0].Role.AdminDesc
          output = '{"error_code":"0", "Response":"Successfully Authenticated for user: %s ","Role":"%s"}' %(username,role)
          logging.debug("login:"+ output)
          return HttpResponse(output)

     else:
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:Failed to Authenticate"+ output)
        return HttpResponse(output)    
   
    
   else:
      logging.debug("login: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("login:"+ output)
      return HttpResponse(output)
###################getRoles####################################
def get_roles(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_roles: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_roles - Unable to Authenticate/get_roles... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_roles:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_roles:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_roles:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_roles:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_roles:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_roles:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_roles_rec = AC_Admin.objects.filter(**kwargs)
        if(len(get_roles_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d roles", \n "get_roles":' %len(get_roles_rec)
           output += '['
           counter = 0
           for rec in get_roles_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"role_id":"%s","role_desc":"%s"}' %(rec.AdminId ,rec.AdminDesc)
              else: 
                output += ',\n {"role_id":"%s","role_desc":"%s"}' %(rec.AdminId ,rec.AdminDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_roles:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the role records, NO_DATA_FOUND"}' 
           logging.debug("get_roles:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_roles:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_roles:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the roles"}' 
         logging.debug("get_roles:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_roles: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_roles:"+ output)
      return HttpResponse(output)
####################get premise#################
def get_premise(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_premise - Unable to Authenticate/get_premise... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_premise:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_premise_rec = AC_Premise.objects.filter(**kwargs)
        if(len(get_premise_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d premise", \n "get_premise":' %len(get_premise_rec)
           output += '['
           counter = 0
           for rec in get_premise_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"premise_id":"%s","premise_desc":"%s"}' %(rec.PremiseId ,rec.PremiseDesc)
              else: 
                output += ',\n {"premise_id":"%s","premise_desc":"%s"}' %(rec.PremiseId ,rec.PremiseDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the premise records, NO_DATA_FOUND"}' 
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_premise:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_premise:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the premise"}' 
         logging.debug("get_premise:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_premise:"+ output)
      return HttpResponse(output)
######################################get units########################
def get_units(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_units: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_units - Unable to Authenticate/get_units... "
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_units:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_units:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_units:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_units:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_units:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_units:"+ output)
        return HttpResponse(output)



     try:
     #{
        results=AC_Unit_History.objects.filter(Temp__range=(23,25)).count()
 
        #results = Oyo_Unit_History.objects.all().values('Temp').annotate(total=Count('Temp')).order_by()

#        query = (Oyo_Unit_History.objects.filter(Temp__gte=23,Temp__lte=25).query).count()
 #       query.group_by = ['CityId']
 #       results = QuerySet(query=query, model=Oyo_Unit_History)        
        print "thsis is results ",results
        #comment 
        kwargs = {}
        floor=''
	premise=''
        
	if((data1.get('FloorId') is None) or ((data1.get('FloorId') is not  None) and (len(data1['FloorId']) <= 0))):
           output_str += ",FloorId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_units:"+ output)
           return HttpResponse(output)
        else:
           floor = data1['FloorId']
           kwargs['FloorId'] = floor

        if((data1.get('FloorId') is not  None) and (len(data1['FloorId']) > 0)):
           floor = data1['FloorId']   
           kwargs['FloorId'] = floor
        
        if((data1.get('PremiseId') is not  None) and (len(data1['PremiseId']) > 0)):
           premise = data1['PremiseId']     
           kwargs['PremiseId'] = premise

        
        get_units_rec = Oyo_Units.objects.filter(**kwargs)
        if(len(get_units_rec) > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d units", \n "get_units":' %len(get_units_rec)
           output += '['
           counter = 0
           for rec in get_units_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"Unit_id":"%s","Premise_id":"%s","Floor_id":"%s","Room_id":"%s","Ipunit_id":"%s","Opunit_id":"%s","Temp":"%s","CreateDate":"%s"}' %(rec.UnitId ,rec.PremiseId.PremiseId,rec.FloorId.FloorId,rec.RoomId.RoomId,rec.IpmacId.IpmacId,rec.OpmacId.OpmacId,rec.Temp,rec.ChangeDate)
              else:
                output += ',\n {"Unit_id":"%s","Premise_id":"%s","Floor_id":"%s","Room_id":"%s","Ipunit_id":"%s","Opunit_id":"%s","Temp":"%s","CreateDate":"%s"}' %(rec.UnitId ,rec.PremiseId.PremiseId,rec.FloorId.FloorId,rec.RoomId.RoomId,rec.IpmacId.IpmacId,rec.OpmacId.OpmacId,rec.Temp,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_units:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the unit records, NO_DATA_FOUND"}'
           logging.debug("get_units:"+ output)
           return HttpResponse(output)
     #}#Comment
     except Exception, e:
     #{
         err_desc = 'get_units:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_units:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the units"}'
         logging.debug("get_units:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_units: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("get_units:"+ output)
      return HttpResponse(output)


###############################################################
def get_floors(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_floors: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_floors - Unable to Authenticate/get_floors... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_floors:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_floors:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_floors:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_floors:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_floors:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_floors:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_floors_rec = AC_Floors.objects.filter(**kwargs)
        if(len(get_floors_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d floors", \n "get_floors":' %len(get_floors_rec)
           output += '['
           counter = 0
           for rec in get_floors_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"floor_id":"%s","floor_desc":"%s"}' %(rec.FloorId ,rec.FloorDesc)
              else: 
                output += ',\n {"floor_id":"%s","floor_desc":"%s"}' %(rec.FloorId ,rec.FloorDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the floors records, NO_DATA_FOUND"}' 
           logging.debug("get_floors:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_floors:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_floors:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the floors"}' 
         logging.debug("get_floors:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_floors: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_floors:"+ output)
      return HttpResponse(output)
#######################################################################
def get_rooms(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_rooms: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_rooms - Unable to Authenticate/get_rooms... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_rooms:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_rooms:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_rooms:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_rooms:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
        
        kwargs = {}
        floor=''
        if((data1.get('FloorId') is not  None) and (len(data1['FloorId']) > 0)):
           floor = data1['FloorId']
           kwargs['FloorId'] = floor    
        #Get the Curent_Status records
        get_rooms_rec = AC_Floor_Room.objects.filter(**kwargs)
        if(len(get_rooms_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d rooms", \n "get_rooms":' %len(get_rooms_rec)
           output += '['
           counter = 0
           for rec in get_rooms_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"Room_id":"%s","Room_desc":"%s"}' %(rec.RoomId.RoomId ,rec.RoomId.RoomDesc)
              else: 
                output += ',\n {"Room_id":"%s","Room_desc":"%s"}' %(rec.RoomId.RoomId ,rec.RoomId.RoomDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_rooms:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the roooms records, NO_DATA_FOUND"}' 
           logging.debug("get_rooms:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_rooms:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_rooms:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the rooms"}' 
         logging.debug("get_rooms:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_rooms: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_rooms:"+ output)
      return HttpResponse(output)
################################################################
def get_units_details(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_units_details: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_units_details - Unable to Authenticate/get_units_details... "
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_units_details:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_units_details:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_units_details:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_units_details:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_units:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if AC_Users.objects.filter(Username = username,Password=password,Role=1).exists():

        is_rec_needed = True
        #print("matching")
     else:
        is_rec_needed = False
        output = '{"error_code":"4", "error_desc": "Response= You have No right to Get/Add/Modify."}'
        logging.debug("get_units_details:"+ output)
        return HttpResponse(output)



     try:
     #{

        kwargs = {}
        floor=''
	premise=''
        
	if((data1.get('UnitId') is None) or ((data1.get('UnitId') is not  None) and (len(data1['UnitId']) <= 0))):
           output_str += ",UnitId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_units_details:"+ output)
           return HttpResponse(output)
        else:
           unitid = data1['UnitId']
           #kwargs['FloorId'] = floor
	#Comments
        if((data1.get('FloorId') is not  None) and (len(data1['FloorId']) > 0)):
           floor = data1['FloorId']   
           kwargs['FloorId'] = floor
        
        if((data1.get('PremiseId') is not  None) and (len(data1['PremiseId']) > 0)):
           premise = data1['PremiseId']     
           kwargs['PremiseId'] = premise
        #comments 
           
        get_units_rec = AC_Unit_Details.objects.filter(UnitId=unitid)
        if(len(get_units_rec) > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d units", \n "get_units_details":' %len(get_units_rec)
           output += '['
           counter = 0
           for rec in get_units_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"Fan":"%s","Status":"%s","Temp":"%s","SetTemp":"%s","Runtime":"%s","Strength":"%s"}' %(rec.Fan ,rec.Status,rec.Temp,rec.SetTemp,rec.Runtime,rec.Strength)
              else:
                output += ',\n {"Fan":"%s","Status":"%s","Temp":"%s","SetTemp":"%s","Runtime":"%s","Strength":"%s"}' %(rec.Fan ,rec.Status,rec.Temp,rec.SetTemp,rec.Runtime,rec.Strength)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_units_details:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the unit records, NO_DATA_FOUND"}'
           logging.debug("get_units_details:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_units_details:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_units_details:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the units details"}'
         logging.debug("get_units_details:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_units_details: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("get_units_details:"+ output)
      return HttpResponse(output)
'''
################### delete Premise######################################
def delete_premise(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_premise- Unable to Authenticate/del_premise... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_premise:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_premise:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_premise:input: user="+username)
   
   
     try:
     #{ 
        
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_premise"}'
          logging.debug("del_premise:"+ output)
          return HttpResponse(output)



        if((data1.get('premise_id') is None) or ((data1.get('premise_id') is not  None) and (len(data1['premise_id']) <= 0))):
           output_str += ", premise_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("premise_id:"+ output)
           return HttpResponse(output)
        else:
           pid = data1['premise_id']   
        #del from DB
        curr_status_recs_get = AC_Premise.objects.filter(PremiseId=pid).delete()
        
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the premise"}'
           logging.debug("del_premise:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_premise"}' 
           logging.debug("del_premise:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_premise:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_premise:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to del the user"}' 
         logging.debug("del_premise:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_premise:"+ output)
      return HttpResponse(output)

############################# delete city ###########################
def delete_city(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("delete_city: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "delete_city- Unable to Authenticate/delete_city... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("delete_city:"+ output)
        return HttpResponse(outputgid)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("delete_city:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("delete_city:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("delete_city:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("delete_city:input: user="+username)
   
   
     try:
     #{ 
        
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_city"}'
          logging.debug("delete_city:"+ output)
          return HttpResponse(output)



        if((data1.get('city_id') is None) or ((data1.get('city_id') is not  None) and (len(data1['city_id']) <= 0))):
           output_str += ", city_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("delete_city:"+ output)
           return HttpResponse(output)
        else:
           cid = data1['city_id']   
        #del from DB
        curr_status_recs_get = AC_City.objects.filter(CityId=cid).delete()
        
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the city"}'
           logging.debug("delete_city:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_city"}' 
           logging.debug("delete_city:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'delete_city:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_premise:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to delete the city"}' 
         logging.debug("delete_city:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("delete_city: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("delete_city:"+ output)
      return HttpResponse(output)

################### delete floor######################################
def delete_floor(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_floor: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_floor- Unable to Authenticate/del_floor... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_floor:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_floor:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_floor:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_floor:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_floor:input: user="+username)
   
   
     try:
     #{ 
        
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_floor"}'
          logging.debug("del_floor:"+ output)
          return HttpResponse(output)



        if((data1.get('floor_id') is None) or ((data1.get('floor_id') is not  None) and (len(data1['floor_id']) <= 0))):
           output_str += ", floor_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("floor_id:"+ output)
           return HttpResponse(output)
        else:
           fid = data1['floor_id']   
        #del from DB
        curr_status_recs_get = AC_Floors.objects.filter(FloorId=fid).delete()
        
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the floor"}'
           logging.debug("del_floors:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_floor"}' 
           logging.debug("del_floor:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_floors:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_floors:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to del the floor"}' 
         logging.debug("del_floor:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_floor:"+ output)
      return HttpResponse(output)

############################# delete room #####################################
def delete_room(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_room: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_room- Unable to Authenticate/del_room... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_room:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_room:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_room:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_room:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_room:input: user="+username)
   
   
     try:
     #{ 
        
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_room"}'
          logging.debug("del_room:"+ output)
          return HttpResponse(output)



        if((data1.get('room_id') is None) or ((data1.get('room_id') is not  None) and (len(data1['room_id']) <= 0))):
           output_str += ", room_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("del_room:"+ output)
           return HttpResponse(output)
        else:
           rid = data1['room_id']   
        #del from DB
        curr_status_recs_get = AC_Rooms.objects.filter(RoomId=rid).delete()
        
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the rooms"}'
           logging.debug("del_rooms:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_rooms"}' 
           logging.debug("del_rooms:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_rooms:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_rooms:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to del the rooms"}' 
         logging.debug("del_rooms:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_rooms: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_rooms:"+ output)
      return HttpResponse(output)

############################# delete unit #####################################
def delete_unit(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_unit: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_unit- Unable to Authenticate/del_unit... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_unit:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_unit:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_unit:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_unit:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_unit:input: user="+username)
   
   
     try:
     #{ 
        
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_room"}'
          logging.debug("del_unit:"+ output)
          return HttpResponse(output)



        if((data1.get('unit_id') is None) or ((data1.get('unit_id') is not  None) and (len(data1['unit_id']) <= 0))):
           output_str += ", unit_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("del_unit:"+ output)
           return HttpResponse(output)
        else:
           uid = data1['unit_id']   
        #del from DB
        curr_status_recs_get = AC_Units.objects.filter(UnitId=uid).delete()
        
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the unit"}'
           logging.debug("del_unit:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_unit"}' 
           logging.debug("del_unit:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_unit:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_unit:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to del the unit"}' 
         logging.debug("del_unit:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_unit: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_unit:"+ output)
      return HttpResponse(output)


############################# delete unit types#####################################
def delete_unit_utype(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_unit_utype: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_unit_utype Unable to Authenticate/del_unit_utype... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_unit_utype:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_unit_utype:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_unit_utype:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_unit_utype:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_unit_utype: user="+username)
   
   
     try:
     #{ 
        ip1=False
        op1=False
        p1=False   
        if AC_Users.objects.filter(Username = username).exists() and AC_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          #print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to del_unit_utype"}'
          logging.debug("del_unit_utype:"+ output)
          return HttpResponse(output)

        if((data1.get('utype') is None) or ((data1.get('utype') is not  None) and (len(data1['utype']) <= 0))):
           output_str += ", utype is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("del_unit_utype:"+ output)
           return HttpResponse(output)
        else:
           utype = data1['utype']
           if utype=="Input":
              ip1=True
           if utype=="Operate":
              op1=True
           if utype=="Power":
              p1=True

        if((data1.get('id') is None) or ((data1.get('id') is not  None) and (len(data1['id']) <= 0))):
           output_str += ", id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("del_unit_utype:"+ output)
           return HttpResponse(output)
        else:
           uid = data1['id']   
        #del from DB
        curr_status_recs_get=''
        if ip1==True:
           #print "input delete "
           curr_status_recs_get = AC_Input_Units.objects.filter(IpId=uid,ChangeBy=username).delete()
        if op1==True:
           #print "opearet delete"
           curr_status_recs_get = AC_Operate_Units.objects.filter(OpId=uid,ChangeBy=username).delete()
        if p1==True:
           #print "power delete "
           curr_status_recs_get = AC_Power_Units.objects.filter(PId=uid,ChangeBy=username).delete()
          
 #       print(curr_status_recs_get) 
        if(len(curr_status_recs_get) > 0 ): #just check con         
           is_history_rec_needed = False
  #         print("success")
          
           output = '{"error_code":"0", "error_desc": "Response=Successfully deleted the unit"}'
           logging.debug("del_unit_utype:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to del_unit"}' 
           logging.debug("del_unit_utype:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_unit:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_unit_utype:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to del the unit"}' 
         logging.debug("del_unit_utype:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_unit: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_unit_utype:"+ output)
      return HttpResponse(output)



'''
#################################get temp history ####################
def get_temp_history(request):
    stdt="2018-09-20 00:00"
    enddt="2018-09-25 23:59"
    start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    data1 = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    #data1 = Oyo_Unit_History.objects.filter()
    grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d %H:%M"))
    jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped]
    extra_context = {"data": data1}
    #print extra_context
    return render(request,"get_temp_history.html", extra_context)



def get_data(request):
    stdt="2018-09-20 00:00"
    enddt="2018-09-25 23:59"
    start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    #data1 = Oyo_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    #data1 = Oyo_Unit_History.objects.filter()
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped] #
    #last_14_days = datetime.today() - datetime.timedelta(14)
    jobs = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).values("ChangeDate")
    grouped = itertools.groupby(jobs, lambda record: record.get("ChangeDate").strftime("%Y-%m-%d"))
    jobs_by_day = [(hour, len(list(jobs_this_day))) for hour, jobs_this_day in grouped]

    extra_context = {"data": jobs_by_day}
    #print extra_context
    return render(request,"get_data.html", extra_context)
'''
def get_power_data(request):
    stdt="2018-09-20 00:00"
    enddt="2018-09-25 23:59"
    start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    #data1 = Oyo_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    data1 = AC_Power_History.objects.filter(PId=15)
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped] #
    #last_14_days = datetime.today() - datetime.timedelta(14)
    #jobs = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).values("ChangeDate")
    #grouped = itertools.groupby(jobs, lambda record: record.get("ChangeDate").strftime("%Y-%m-%d"))
    #jobs_by_day = [(hour, len(list(jobs_this_day))) for hour, jobs_this_day in grouped]

    extra_context = {"data": data1}
    #print extra_context
    return render(request,"power_check.html", extra_context)


######################################dropdown#####################
def get_drop_down(request):
    stdt="2018-09-20 00:00"
    enddt="2018-09-25 23:59"
    start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    #data1 = Oyo_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    data1 = AC_Input_Units.objects.filter()
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped] #
    #last_14_days = datetime.today() - datetime.timedelta(14)
    #jobs = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).values("ChangeDate")
    #grouped = itertools.groupby(jobs, lambda record: record.get("ChangeDate").strftime("%Y-%m-%d"))
    #jobs_by_day = [(hour, len(list(jobs_this_day))) for hour, jobs_this_day in grouped]

    extra_context = {"data": data1}
    #print extra_context
    return render(request,"dropdown.html", extra_context)

def get_data(request):
    if(request.method == "POST"):
       a = request.POST['drop1']
       extra_context = {"data": a}
       #print extra_context
       return render(request,"dropdown_success.html", extra_context)       
    else:
       data1 = request.POST['drop1']
       data2=request.POST['drop2']
       data='{"%s":"%s"}' %(data1,data2) 
       extra_context = {"data": data}
       #print extra_context
       return render(request,"dropdown_success.html", extra_context)
       #context_dict = {}
       #return render(request, 'redirect.html', context_dict)
#################### upload images#######################################
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



