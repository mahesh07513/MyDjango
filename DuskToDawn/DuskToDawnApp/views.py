from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from DuskToDawnApp.models import *
from django.http import HttpResponse
from django.http import JsonResponse
import json
import logging
from django.db.models import *
import urllib2
from datetime import datetime
import datetime as dt1
import time
import sys
######################################################
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
     '''	
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:Failed to Authenticate"+ output)
        return HttpResponse(output)
     else:
        output = '{"error_code":"0", "error_desc": "Response=Successfully Authenticated login"}' 
        logging.debug("login:"+ output)
        return HttpResponse(output)
     '''
     if Login_Users.objects.filter(Uname = username,Pass=password).exists():
     #{
          print("yes")
          #print(AdminSupp.objects.values('uname'))
          output = '{"error_code":"0", "Response":"Successfully Authenticated for user: %s "}' %(username)
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
####################delete unit ############################################################
def delete_unit(request):  #this will del

   if(request.method == "POST"):
   #{
     logging.debug("del_unit: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_unit- Unable to Authenticate/del_unit... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
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

        if DtD_Users.objects.filter(Username = username).exists() and DtD_Users.objects.filter(Password = password).exists():
    # at least one object satisfying query exists
          print("yes")
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
        curr_status_recs_get = DtD_Units.objects.filter(UnitId=uid).delete()

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
