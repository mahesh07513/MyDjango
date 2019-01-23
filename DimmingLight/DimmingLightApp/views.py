from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from DimmingLightApp.models import *
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
# Create your views here.
##############################################################################################

def add_modes(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_modes: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_modes - Unable to Authenticate/add_modes... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_modes:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_modes:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_curr_status:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_curr_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']        

     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_modes:Failed to Authenticate"+ output)
        return HttpResponse(output)   


     if((data1.get('Modes') is None) or ((data1.get('Modes') is not  None) and (len(data1['Modes']) <= 0))):
           output_str += ", Modes is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
     else:

        modes = data1['Modes'] 

     if((data1.get('Esps') is None) or ((data1.get('Esps') is not  None) and (len(data1['Esps']) <= 0))):
           output_str += ", Esps is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
     else:
        esps = data1['Esps']

     if((data1.get('Time_Dim') is None) or ((data1.get('Time_Dim') is not  None) and (len(data1['Time_Dim']) <= 0))):
           output_str += ", Time_Dim is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
     else:
        time = data1['Time_Dim']  
  
     if((data1.get('Light_Dim') is None) or ((data1.get('Light_Dim') is not  None) and (len(data1['Light_Dim']) <= 0))):
           output_str += ", Light_Dim is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
     else:
        light = data1['Light_Dim']


     date1 = datetime.today()
     todaytime = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')     
   
     try:
     #{
        '''
        save_user = Login_Users(Uname=username,Pass=password,ChangeDate=todaytime);
        save_user.save()
        if save_user > 0:  
           output = '{"error_code":"0", "error_desc": "Response=Successfully added the User = %s"}' %(username)
           logging.debug("add_modes:"+ output)
           return HttpResponse(output) 
        '''

        check_status = False
        '''
        curr_mode_recs_get = Dim_Modes.objects.filter(Modes=modes)
        if(len(curr_mode_recs_get) > 0): #just update the ChangeDate         
           check_status = True
        '''   
        
        #Add the  record
        #print("in side",esps,modes,time,light)
        esps = str(esps)[1:-1]
        time = str(time)[1:-1]
        light = str(light)[1:-1]
        #print("remove ",esps,time,light)
        curr_modes_esp_rec = Dim_Esps(Esps=esps,Modes=modes,Time=time,Light_dim=light);
        #print("1")
        curr_modes_esp_rec.save()
        #print("2")
        if(curr_modes_esp_rec > 0):
           #print("3")
           output = '{"error_code":"0", "Response":"Successfully added the modes settings, Mode=%s"}' %(modes)
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add Modes"}' 
           logging.debug("add_modes:"+ output)
           return HttpResponse(output)
      
        


     #}
     except Exception, e:
     #{
         err_desc = 'add_modes:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_modes:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the Modes"}' 
         logging.debug("add_modes:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_modes: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_modes:"+ output)
      return HttpResponse(output)


########################################################################

def get_modes(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_modes: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_modes- Unable to Authenticate/get_modes... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_modes:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_modes:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_modes:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_modes:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_modes:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_modes:Failed to Authenticate"+ output)
        return HttpResponse(output)
      
   
     try:
     #{
        towerid = ""   
        status = ""
        kwargs = {}
        check_login_authenticate=True
        '''
        if AdminSupp.objects.filter(uname = username).exists() and AdminSupp.objects.filter(upass = password).exists():
    # at least one object satisfying query exists
          print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to get user details"}'
          logging.debug("add_user:"+ output)
          return HttpResponse(output)
	
        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        if((data1.get('Status') is not  None) and (len(data1['Status']) > 0)):
           status = data1['Status']   
           kwargs['Status'] = status
        '''
        #Get the Curent_Status records
        curr_status_recs =Dim_Esps.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d modes", \n "get_modes":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"modes":"%s"}' %(rec.Modes)
              else: 
                output += ',\n {"modes":"%s"}' %(rec.Modes)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_modes:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the get_modes records, NO_DATA_FOUND"}' 
           logging.debug("get_modes:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_modes:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_modes:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the get_modes"}' 
         logging.debug("get_modes:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_modes: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_modes:"+ output)
      return HttpResponse(output)

#######################################################################################
def get_mode_settings(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_mode_settings: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_mode_settings- Unable to Authenticate/get_curr_status... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_mode_settings:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_mode_settings:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_mode_settings:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_mode_settings:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_mode_settings:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_mode_settings:Failed to Authenticate"+ output)
        return HttpResponse(output)
      
   
     try:
     #{
        towerid = ""   
        status = ""
        kwargs = {}
        check_login_authenticate=True
        '''
        if AdminSupp.objects.filter(uname = username).exists() and AdminSupp.objects.filter(upass = password).exists():
    # at least one object satisfying query exists
          print("yes")
          #print(AdminSupp.objects.values('uname'))
          check_login_authenticate=False
        else:
          output = '{"error_code":"3", "error_desc": "Your not a admin to get user details"}'
          logging.debug("add_user:"+ output)
          return HttpResponse(output)
	
        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        if((data1.get('Status') is not  None) and (len(data1['Status']) > 0)):
           status = data1['Status']   
           kwargs['Status'] = status
       '
        if((data1.get('Modes') is None) or ((data1.get('Modes') is not  None) and (len(data1['Modes']) <= 0))):
           output_str += ", Modes is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_mode_settings:"+ output)
           return HttpResponse(output)
        else:
           modes = data1['Modes']
        '''

        if((data1.get('Modes') is not  None) and (len(data1['Modes']) > 0)):
           modes = data1['Modes']   
           kwargs['Modes'] = modes
        #Get the Curent_Status records
        curr_status_recs =Dim_Esps.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d modes", \n "get_modes":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"modes":"%s","esps":"[%s]","times":"[%s]","lights":"[%s]"}' %(rec.Modes,rec.Esps,rec.Time,rec.Light_dim)
              else: 
                output += ',\n {"modes":"%s","esps":"[%s]","times":"[%s]","lights":"[%s]"}' %(rec.Modes,rec.Esps,rec.Time,rec.Light_dim)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_mode_settings:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the get_mode_settings records, NO_DATA_FOUND"}' 
           logging.debug("get_mode_settings:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_mode_settings:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_mode_settings:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the get_mode_settings"}' 
         logging.debug("get_mode_settings:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_mode_settings: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_mode_settings:"+ output)
      return HttpResponse(output)





