from __future__ import unicode_literals
from django.shortcuts import render
#from datetime import tzinfo,timedelta
import requests
# Create your views here.
from PrepaidRCApp.models import *
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

#############################
def add_charge(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_charge: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_charge- Unable to Authenticate/add_charge... "
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_charge:"+ output)
        HttpResponse(output)

     
     #check authentication (temporary, this will need to be implemented)
    
     try:
     #{
        if((data1.get('username') is None) or ((data1.get('username') is not  None) and (len(data1['username']) <= 0))):
           output_str += ",username is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_charge:"+ output)
           return HttpResponse(output)
        else:
           uname = data1['username']

        if((data1.get('Phone') is None) or ((data1.get('Phone') is not  None) and (len(data1['Phone']) <= 0))):
           output_str += ",Phone is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_charge:"+ output)
           return HttpResponse(output)
        else:
           phone = data1['Phone']

        if((data1.get('Cat') is None) or ((data1.get('Cat') is not  None) and (len(data1['Cat']) <= 0))):
           output_str += ",Cat is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_charge:"+ output)
           return HttpResponse(output)
        else:
           Cat = data1['Cat']

        

        if((data1.get('paid') is None) or ((data1.get('paid') is not  None) and (len(data1['paid']) <= 0))):
           output_str += ",paid is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_charge:"+ output)
           return HttpResponse(output)
        else:
           paid = data1['paid']
           #units = int(paid)/5
        kwargs = {}
       
        if Cat==str(1):
            get_rec=Prepaid_Cat_Fares.objects.filter(**kwargs)
            print get_rec[0].Domestic
            if(len(get_rec) > 0):
               unitPriceDom=get_rec[0].Domestic
               unitsDom=get_rec[0].Units
               unitPrice1=get_rec[1].Domestic
               units1=get_rec[1].Units
               cost=unitsDom*unitPriceDom
               print unitPriceDom,unitsDom,unitPrice1,units1,cost,paid
               if float(paid)<float(cost):
                  unitCount=float(paid)/float(unitPriceDom)
                  print unitCount
               else:
                  pricediff= float(paid)-float(cost)
                  unitCount1=pricediff/unitPrice1
                  unitCount=unitsDom+unitCount1
                  print pricediff,unitCount1,unitCount
                 
               output = '{"error_code":"0", "Response":"Your Recharege is Successfully " , "units":"%s"}' %(round(unitCount))
               logging.debug("add_charge:"+ output)
               return HttpResponse(output)

       
        else:
            get_rec=Prepaid_Cat_Fares.objects.filter(**kwargs)
            print get_rec[0].Commercial
            if(len(get_rec) > 0):
               unitPriceCom=get_rec[0].Commercial
               unitsCom=get_rec[0].Units
               unitPrice1=get_rec[1].Commercial
               units1=get_rec[1].Units
               cost=unitsCom*unitPriceCom
               print unitPriceCom,unitsCom,unitPrice1,units1,cost,paid
               if float(paid)<float(cost):
                  unitCount=float(paid)/float(unitPriceCom)
                  print unitCount
               else:
                  pricediff= float(paid)-float(cost)
                  unitCount1=pricediff/unitPrice1
                  unitCount=unitsCom+unitCount1
                  print pricediff,unitCount1,unitCount

               output = '{"error_code":"0", "Response":"Your Recharege is Successfully " , "units":"%s"}' %(round(unitCount))
               logging.debug("add_charge:"+ output)
               return HttpResponse(output)
  
           
     #}
     except Exception, e:
     #{
         err_desc = 'add_charge:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_charge:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Recharge Failed "}'
         logging.debug("add_charge:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_charge: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_charge:"+ output)
      return HttpResponse(output)
