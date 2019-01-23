#from django.shortcuts import render
from __future__ import unicode_literals
from django.shortcuts import render
#from datetime import tzinfo,timedelta
import requests
# Create your views here.
from UrbanKisanApp.models import *
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
import datetime
import pytz
import sys
import socket

from dateutil import rrule

# Create your views here.
####################### render ##########################################

def get_data(request):
    data1 = UK_Unit_Params.objects.all()
    extra_context = {"data": data1}
    #print extra_context
    return render(request,"get_data.html", extra_context)
def get_history(request):
    data1 = UK_Unit_History.objects.all()
    extra_context = {"data": data1}
    #print extra_context
    return render(request,"get_history.html", extra_context)


#################################  post ######################################
def get_data_UB(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_data_UB: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_data_UB - Unable to Authenticate/get_data_UB... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_data_UB:"+ output)
        return HttpResponse(output)
     
     # if(not data1):
     #    output_str += ", details are mandatory"
     #    output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
     #    logging.debug("get_data_UB:"+ output)
     #    return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_data_UB:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_data_UB:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_data_UB:input: user="+username)

          
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_data_UB_rec = UK_Unit_Params.objects.filter(**kwargs)
        if(len(get_data_UB_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d roles", \n "get_data_UB":' %len(get_data_UB_rec)
           output += '['
           counter = 0
           for rec in get_data_UB_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"unitid":"%s",macid":"%s","temp":"%s","WL":"%s","pH":"%s","Ec":"%s","ppm":"%s","changedate":"%s"}' %(rec.UnitId,rec.MacId,rec.Temp,rec.WaterLevel,rec.Ph,rec.EC,rec.Ppm,rec.ChangeDate)
              else: 
                output += ',\n {"unitid":"%s","macid":"%s","temp":"%s","WL":"%s","pH":"%s","Ec":"%s","ppm":"%s","changedate":"%s"}' %(rec.UnitId,rec.MacId,rec.Temp,rec.WaterLevel,rec.Ph,rec.EC,rec.Ppm,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_data_UB:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the records, NO_DATA_FOUND"}' 
           logging.debug("get_data_UB:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_data_UB:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_data_UB:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the data"}' 
         logging.debug("get_data_UB:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_data_UB: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_data_UB:"+ output)
      return HttpResponse(output)



###########################
def get_history_UB(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_history_UB: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_history_UB - Unable to Authenticate/get_history_UB... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_history_UB:"+ output)
        return HttpResponse(output)
     
     # if(not data1):
     #    output_str += ", details are mandatory"
     #    output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
     #    logging.debug("get_history_UB:"+ output)
     #    return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_history_UB:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_history_UB:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_history_UB:input: user="+username)

          
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_history_UB_rec = UK_Unit_History.objects.filter(**kwargs)
        if(len(get_history_UB_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d roles", \n "get_history_UB":' %len(get_history_UB_rec)
           output += '['
           counter = 0
           for rec in get_history_UB_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"unitid":"%s",macid":"%s","temp":"%s","WL":"%s","pH":"%s","Ec":"%s","ppm":"%s","changedate":"%s"}' %(rec.UnitId,rec.MacId,rec.Temp,rec.WaterLevel,rec.Ph,rec.EC,rec.Ppm,rec.ChangeDate)
              else: 
                output += ',\n {"unitid":"%s",macid":"%s","temp":"%s","WL":"%s","pH":"%s","Ec":"%s","ppm":"%s","changedate":"%s"}' %(rec.UnitId,rec.MacId,rec.Temp,rec.WaterLevel,rec.Ph,rec.EC,rec.Ppm,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_history_UB:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the history, NO_DATA_FOUND"}' 
           logging.debug("get_history_UB:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_history_UB:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_history_UB:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the history"}' 
         logging.debug("get_history_UB:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_history_UB: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_history_UB:"+ output)
      return HttpResponse(output)


