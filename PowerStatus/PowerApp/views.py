# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from PowerApp.models import *
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
import threading
######################################################
def reset_voltage():
  threading.Timer(5.0, reset_voltage).start()
  #print("Hello, World!")

  curr_status_recs = Power_Voltage.objects.filter()
  if(len(curr_status_recs) > 0): 
     for rec in curr_status_recs:
         #print rec.ChangeDate,rec.Power_Id
         pid=rec.Power_Id
         date1 = datetime.today()
         #print date1
         sttime = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S') 
         #print sttime
         #sttime=datetime.strftime(end_date, '%Y-%m-%d %H:%M:%S')
	 endtime=datetime.strftime(rec.ChangeDate, '%Y-%m-%d %H:%M:%S')
	 fmt = '%Y-%m-%d %H:%M:%S'
	 d1 = datetime.strptime(sttime, fmt)
	 d2 = datetime.strptime(endtime, fmt)
	 timediff=int((d1-d2).total_seconds())
         #print timediff
         if timediff >15:
            update=Power_Voltage.objects.filter(Power_Id=pid)
            update.update(Power_Voltage=0,ChangeDate=date1)
#reset_voltage()


def login(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("login: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "login- Unable to Authenticate/login... " 
     try:
        data1 = json.loads(request.body)
	#print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("login:"+ output)
        return HttpResponse(output)
     
     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("login:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("login:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("login:input: user="+username)
     	
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("login:Failed to Authenticate"+ output)
        return HttpResponse(output)
     else:
        output = '{"error_code":"0", "error_desc": "Response=Successfully Authenticated login"}' 
        #logging.debug("login:"+ output)
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
    '''
    
   else:
      #logging.debug("login: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("login:"+ output)
      return HttpResponse(output)
################################################################################

def add_power_voltage(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     #logging.debug("add_power_voltage: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_power_voltage- Unable to Authenticate/add_power_voltage... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("add_power_voltage:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Tower status details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("add_power_voltage:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("add_power_voltage:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        #output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_power_voltage:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     #logging.debug("add_power_voltage:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("add_power_voltage:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     check_login_authenticate=False

     try:
        '''
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           check_login_authenticate=True
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_power_voltage:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''
        if((data1.get('Power_Id') is None) or ((data1.get('Power_Id') is not  None) and (len(data1['Power_Id']) <= 0))):
           output_str += ", Power_Id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           #logging.debug("add_power_voltage:"+ output)
           return HttpResponse(output)
        else:
           powerid = data1['Power_Id']   

        

        if((data1.get('Power_Voltage') is None) or ((data1.get('Power_Voltage') is not  None) and (len(data1['Power_Voltage']) <= 0))):
           output_str += ",Power_Voltage is mandatory "
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           #logging.debug("add_power_voltage:"+ output)
           return HttpResponse(output)
        else:
           pvoltage = data1['Power_Voltage']

     
        #get the status from DB
        is_history_rec_needed = True

        curr_status_recs_get = Power_Voltage.objects.filter(Power_Id=powerid,ChangeBy=username)
        if(len(curr_status_recs_get) > 0): #just update the ChangeDate         
           is_history_rec_needed = False
           
        
        #Add the Curent_Status record
        curr_status_rec = Power_Voltage(Power_Id=powerid, Power_Voltage=pvoltage, ChangeBy=username);
        curr_status_rec.save()
        if(len(str(curr_status_rec.ChangeDate)) > 0): #If there is an exception, it will not come here
        #{
           
           #{
            curr_status_hist_rec = Power_Voltage_History(Power_Id=powerid, Power_Voltage=pvoltage,ChangeBy=username);
            curr_status_hist_rec.save()
            if(curr_status_hist_rec.ActivityId > 0):
               output = '{"error_code":"0", "error_desc": "Response=Successfully added the voltage"}'
               #logging.debug("add_power_voltage:"+ output)
               return HttpResponse(output)
            else:
               output = '{"error_code":"3", "error_desc": "Response=Failed to add voltage History"}' 
               #logging.debug("add_power_voltage:"+ output)
               return HttpResponse(output)
           #}
          
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add voltage"}' 
           #logging.debug("add_power_voltage:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'add_power_voltage:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         #logging.debug("add_power_voltage:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the voltage"}' 
         #logging.debug("add_power_voltage:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      #logging.debug("add_power_voltage: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("add_power_voltage:"+ output)
      return HttpResponse(output)

################################################################################
def get_sumary(request):

   if(request.method == "POST"):
   #{
     #logging.debug("get_sumary: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_sumary- Unable to Authenticate/get_sumary... " 
     try:
        data1 = json.loads(request.body)
        #print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_sumary:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_sumary:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_sumary:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_sumary:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     #logging.debug("get_sumary:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_sumary:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        '''
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''
        powerid = ""   
        status = ""
        

        curr_date = time.strftime('%Y-%m-%d')
        kwargs = {}

        if((data1.get('Power_Id') is not  None) and (len(data1['Power_Id']) > 0)):
           towerid = data1['Power_Id']   
           kwargs['Power_Id'] = towerid
       
          
        if(data1.get('StartDate') is None):
           output_str += ",StartDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           #logging.debug("get_sumary:"+ output)
           return HttpResponse(output)

        if(data1.get('EndDate') is None):
           output_str += ",EndDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           #logging.debug("get_sumary:"+ output)
           return HttpResponse(output)
        start_date  = data1['StartDate']
        end_date    = data1['EndDate']

        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        curr_status_recs = Power_Voltage_History.objects.filter(ChangeBy=username,ChangeDate__range=[start_date, end_date],**kwargs)
# curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=[start_date, end_date]).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]
        #Get the Curent_Status records
        #curr_status_recs = Current_Status_History.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0):
           #print("enter recs") 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d recs", \n "Voltage_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              #print("in for")
              counter += 1
              if(counter == 1):
                #print("in count")
                output += '{"Power_Id":"%s", "Power_Voltage":"%s", "ChangeDate":"%s"}' %(rec.Power_Id, rec.Power_Voltage, rec.ChangeDate) 
              else: 
      #print("in count else")
                output += ',\n {"Power_Id":"%s", "Power_Voltage":"%s", "ChangeDate":"%s"}' %(rec.Power_Id, rec.Power_Voltage,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           #logging.debug("get_sumary:"+ output)
           return HttpResponse(output)
        #}
        else:
           #print("in else")
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the voltage records, NO_DATA_FOUND"}' 
           #logging.debug("get_sumary:"+ output)
           return HttpResponse(output)




     except Exception, e:
     #{
         err_desc = 'get_sumary:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         #logging.debug("get_sumary:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the voltage history "}' 
         #logging.debug("get_sumary:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      #logging.debug("get_sumary: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("get_sumary:"+ output)
      return HttpResponse(output)

######################################################################
def get_last_voltage(request):

   if(request.method == "POST"):
   #{
     #logging.debug("get_last_voltage: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_last_voltage- Unable to Authenticate/get_last_voltage... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_last_voltage:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_last_voltage:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_last_voltage:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_last_voltage:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     #logging.debug("get_last_voltage:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_last_voltage:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''

        powerid = ""   
        
        kwargs = {}
        
        if((data1.get('Power_Id') is not  None) and (len(data1['Power_Id']) > 0)):
           powerid = data1['Power_Id']   
           kwargs['Power_Id'] = powerid

        
        '''
        if((data1.get('username') is not  None) and (len(data1['username']) > 0)):
           uname = data1['username']   
           kwargs['username'] = uname
        '''
        #uname = data1['username']
        #kwargs['username'] = uname   
        #Get the Curent_Status records
        #print("aray data",kwargs)
        curr_status_recs = Power_Voltage.objects.filter(ChangeBy=username,**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           #print("in")
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d modules ", \n "get_last_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"power_id":"%s","voltage":"%s"}' %(powerid,rec.Power_Voltage)
              else: 
                output += ',\n {"power_id":"%s","voltage":"%s"}' %(powerid,rec.Power_Voltage)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           #logging.debug("get_last_voltage:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the voltage records, NO_DATA_FOUND"}' 
           #logging.debug("get_last_voltage:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_last_voltage:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         #logging.debug("get_last_voltage:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the voltage"}' 
         #logging.debug("get_last_voltage:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      #logging.debug("get_last_voltage: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("get_last_voltage:"+ output)
      return HttpResponse(output)



#####################################################
def get_modules(request):

   if(request.method == "POST"):
   #{
     #logging.debug("get_modules: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_modules- Unable to Authenticate/get_modules... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_modules:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        #logging.debug("get_modules:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_modules:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_modules:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     #logging.debug("get_modules:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        #logging.debug("get_modules:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''

        
        
        kwargs = {}
        
        

        
        '''
        if((data1.get('username') is not  None) and (len(data1['username']) > 0)):
           uname = data1['username']   
           kwargs['username'] = uname
        '''
        #uname = data1['username']
        #kwargs['username'] = uname   
        #Get the Curent_Status records
        #print("aray data",kwargs)
        curr_status_recs = Power_Voltage.objects.filter(ChangeBy=username,**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           #print("in")
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d modules ", \n "get_modules_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"Power_Id":"%s"}' %(rec.Power_Id)
              else: 
                output += ',\n {"Power_Id":"%s"}' %(rec.Power_Id)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           #logging.debug("get_modules:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the modules records, NO_DATA_FOUND"}' 
           #logging.debug("get_modules:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_modules:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         #logging.debug("get_modules:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the modules"}' 
         #logging.debug("get_modules:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      #logging.debug("get_modules: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("get_modules:"+ output)
      return HttpResponse(output)

