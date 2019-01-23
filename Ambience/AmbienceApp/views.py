from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from AmbienceApp.models import *
from django.http import HttpResponse
from django.http import JsonResponse
import json
import logging
from django.db.models import *
#import urllib2
from datetime import datetime
#import datetime as dt1
import time
import sys
import socket
import schedule
host = 'jtsha.in'
port = 322
import MySQLdb
import threading

def printit():
  output=''
  threading.Timer(5.0, printit).start()
  print("Hello, World!")
  print(datetime.today())
  date1 = datetime.today()
  #present1 ="2018-01-31 13:03"
  end_date = datetime.strftime(date1, '%Y-%m-%d %H:%M')
  print(end_date)
  curr_setting_recs = Light_Status.objects.all()
  for rec in curr_setting_recs:
      output = '{"esp_id":"%s","cct":"%s","light_intencity1":"%s","changeDate":"%s"}' %(rec.esp_id,rec.cct,rec.light_intencity1,rec.ChangeDate)
     
      time1=rec.ChangeDate
      print(datetime.strftime(time1, '%Y-%m-%d %H:%M'))
      #print(time1.strftime('%Y-%m-%d %H:%M'))
      if end_date == time1.strftime('%Y-%m-%d %H:%M'):
         print("inside")
         print(rec.esp_id) 
      
      print(output) 

#printit()


##########################################################
# def send_request(request):  #this will add/update the status

#    if(request.method == "POST"):
#       print("this is post ")
#       logging.debug("login: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
#       output_str = "login- Unable to Authenticate/login... "
#       try:
#          data1 = json.loads(request.body)
#          #iint request.body
#       except ValueError:
#          output_str += ",invalid input, no proper JSON request "
#          output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
#          logging.debug("login:"+ output)
#          return HttpResponse(output)
#       try:
#          if((data1.get('esp_Id') is None) or ((data1.get('esp_Id') is not  None) and (len(data1['esp_Id']) <= 0))):
#              output_str += ", esp_Id is mandatory"
#              output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
#              logging.debug("del_curr_status:"+ output)
#              return HttpResponse(output)
#          else:
#              espid = data1['esp_Id']

#          if((data1.get('mobile_id') is None) or ((data1.get('mobile_id') is not  None) and (len(data1['mobile_id']) <= 0))):
#              output_str += ", mobile_id is mandatory"
#              output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
#              logging.debug("del_curr_status:"+ output)
#              return HttpResponse(output)
#          else:
#              mobileid = data1['mobile_id']

#          if((data1.get('cct') is None) or ((data1.get('cct') is not  None) and (len(data1['cct']) <= 0))):
#              output_str += ", cct is mandatory"
#              output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
#              logging.debug("del_curr_status:"+ output)
#              return HttpResponse(output)
#          else:
#              cct = data1['cct']
#          if((data1.get('light_intencity') is None) or ((data1.get('light_intencity') is not  None) and (len(data1['light_intencity']) <= 0))):
#              output_str += ", light_intencity is mandatory"
#              output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
#              logging.debug("del_curr_status:"+ output)
#              return HttpResponse(output)
#          else:
#              lightintencity = data1['light_intencity']

#          add_recs = Light_Status(esp_Id=espid,mobile_id=mobileid,cct=cct,light_intencity=lightintencity);
#          add_recs.save()
#          if(add_recs > 0):
#             output = '{"error_code":"0", "error_desc": "Response=Successfully added the Current_Status, Status=%s"}' %(espid)
#             logging.debug("add_curr_status:"+ output)
#             return HttpResponse(output)
#          else:
#              output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status History"}'
#              logging.debug("add_curr_status:"+ output)
#              return HttpResponse(output)



#       except Exception:
#      #{
#         err_desc = 'add_curr_status:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
#         logging.debug("add_curr_status:"+ err_desc)
#         output = '{"error_code":"3", "error_desc": "Response=Failed to add the Status"}'
#         logging.debug("add_curr_status:"+ output)
#         return HttpResponse(output)

#    else:

#       print("this is get ")
#       s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#       result = s.connect_ex((host, port))
#       s.close()
#       if result:
#        # print "problem with socket!"
#          output="problem with socket!"
#       else:
#         #print "everything it's ok!"
#      #ng.debug("send_request: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
#       #utput="everything it's ok!"

#       #tput = '{"error_code":"0", "error_desc": "Response="'+output+'}'
#       #ogging.debug("send_request:"+ output)
#      #return HttpResponse(output)

########################################################################
def get_current_setting(request):  # this will user acces group

   if(request.method == "POST"):
   #{
     logging.debug("get_current_setting: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_current_setting- Unable to Authenticate/get_current_setting... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_current_setting:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", all details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_current_setting:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_current_setting:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_current_setting:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_current_setting:input: user="+username)

     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_current_setting:Failed to Authenticate"+ output)
        return HttpResponse(output)


     try:
     #{



        if((data1.get('esp_id') is not  None) and (len(data1['esp_id']) > 0)):
           espid = data1['esp_id']

           print(espid)
        #Get the Curent_Status records
        curr_setting_recs = Light_Status.objects.filter(esp_Id=espid)
        print(curr_setting_recs)
        if(curr_setting_recs > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d user groups ", \n "get_current_setting":' %len(curr_setting_recs)
           output += '['
           counter = 0
           for rec in curr_setting_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"esp_id":"%s","cct":"%s","light_intencity":"%s"}' %(rec.esp_Id,rec.cct,rec.light_intencity)
              else:
                output += ',\n {"esp_id":"%s","cct":"%s","light_intencity":"%s"}' %(rec.esp_Id,rec.cct,rec.light_intencity)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_current_setting:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the light settings, NO_DATA_FOUND"}'

           logging.debug("get_current_setting:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
     #{
         err_desc = 'get_current_setting:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_current_setting:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the light details "}'
         logging.debug("get_current_setting:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_current_setting: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("get_current_setting:"+ output)
      return HttpResponse(output)

############################################################################
def add_light_position(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_light_position: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_light_position- Unable to Authenticate/add_light_position... "
     try:
        data1 = json.loads(request.body)
       #print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_light_position:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_light_position:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_light_position:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_light_position:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("add_light_position:input: user="+username)

     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_light_position:Failed to Authenticate"+ output)
        return HttpResponse(output)


     try:
        '''
        if(data1.get('date1') is None):
           output_str += ",datetime is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        datafromuser=data1['date1']
        '''
     #{
        if((data1.get('esp_id') is None) or ((data1.get('esp_id') is not  None) and (len(data1['esp_id']) <= 0))):
           output_str += ",esp_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           espid = data1['esp_id']

        if((data1.get('mobile_id') is None) or ((data1.get('mobile_id') is not  None) and (len(data1['mobile_id']) <= 0))):
           output_str += ",mobile_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           mobileid = data1['mobile_id']

        if((data1.get('cct') is None) or ((data1.get('cct') is not  None) and (len(data1['cct']) <= 0))):
           output_str += ",cct is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           cct = data1['cct']

        if((data1.get('light_intencity1') is None) or ((data1.get('light_intencity1') is not  None) and (len(data1['light_intencity1']) <= 0))):
           output_str += ",light_intencity1  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           lightintencity1  = data1['light_intencity1']
        
        if((data1.get('light_intencity2') is None) or ((data1.get('light_intencity2') is not  None) and (len(data1['light_intencity2']) <= 0))):
           output_str += ",light_intencity2  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           lightintencity2  = data1['light_intencity2']


        if((data1.get('light_intencity3') is None) or ((data1.get('light_intencity3') is not  None) and (len(data1['light_intencity3']) <= 0))):
           output_str += ",light_intencity3  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           lightintencity3  = data1['light_intencity3']
        

        #get the status from DB

        check_rec = Light_Status.objects.filter(esp_id=espid)
        
        if(len(check_rec)>0): #just update
          
           output = '{"error_code":"4", "error_desc": "Response= Your esp id is alreay exists Please change."}'
           logging.debug("add_group:"+ output)
           return HttpResponse(output)
        
        add_light_rec = Light_Status(esp_id=espid,mobile_id=mobileid,cct=cct,light_intencity1=lightintencity1,light_intencity2=lightintencity2,light_intencity3=lightintencity3);
        print("1")
        add_light_rec.save()
        print("2")
        print(add_light_rec)
        if(len(str(add_light_rec)) > 0):
           output = '{"error_code":"0", "Response":"Successfully added the light settings for esp = %s"}' %(espid) 
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add Current settings"}'
           logging.debug("add_light_position:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
     #{
         err_desc = 'add_light_position:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_light_position:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the current settings1"}'
         logging.debug("add_light_position:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_light_position: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_light_position:"+ output)
      return HttpResponse(output)

################################################################
def get_org_type(request):  # this will user acces group


   if(request.method == "POST"):
   #{
     logging.debug("get_org_type: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_org_type- Unable to Authenticate/get_org_type... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_org_type:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", all details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_org_type:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_org_type:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_org_type:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_org_type:input: user="+username)

     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_org_type:Failed to Authenticate"+ output)
        return HttpResponse(output)


     try:
     #{
	kwgrs={}


        
        #Get the Curent_Status records
        curr_setting_recs = Light_Org_Types.objects.filter(**kwgrs)
        print(curr_setting_recs)
        if(curr_setting_recs > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d org type ", \n "get_org_type":' %len(curr_setting_recs)
           output += '['
           counter = 0
           for rec in curr_setting_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"org_tid":"%s","org_type":"%s"}' %(rec.OrgTypeId,rec.OrgTypeDesc)
              else:
                output += ',\n {"org_tid":"%s","org_type":"%s"}' %(rec.OrgTypeId,rec.OrgTypeDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_org_type:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the org type, NO_DATA_FOUND"}'

           logging.debug("get_org_type:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
     #{
         err_desc = 'get_org_type:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_org_type:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the org type "}'
         logging.debug("get_org_type:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_org_type: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("get_org_type:"+ output)
      return HttpResponse(output)
################################################################
def get_orgs(request):  # this will user acces group


   if(request.method == "POST"):
   #{
     logging.debug("get_orgs: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_orgs- Unable to Authenticate/get_orgs... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_orgs:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", all details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_orgs:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_orgs:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_orgs:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_orgs:input: user="+username)

     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_orgs:Failed to Authenticate"+ output)
        return HttpResponse(output)


     try:
     #{
	kwgrs={}


        
        #Get the Curent_Status records
        curr_setting_recs = Light_Orgs.objects.filter(**kwgrs)
        print(curr_setting_recs)
        if(curr_setting_recs > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d org names ", \n "get_org_names":' %len(curr_setting_recs)
           output += '['
           counter = 0
           for rec in curr_setting_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"org_id":"%s","org_name":"%s"}' %(rec.OrgId,rec.OrgDesc)
              else:
                output += ',\n {"org_id":"%s","org_name":"%s"}' %(rec.OrgId,rec.OrgDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_orgs:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the org names, NO_DATA_FOUND"}'

           logging.debug("get_orgs:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
     #{
         err_desc = 'get_orgs:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_orgs:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the org names "}'
         logging.debug("get_orgs:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_org_type: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("get_orgs:"+ output)
      return HttpResponse(output)



#################################################################
def add_user(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_user: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_user - Unable to Authenticate/add_user... "
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     if(data1.get('Username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
     logging.debug("add_user:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''

     try:

        
     #{
        if((data1.get('Name') is None) or ((data1.get('Name') is not  None) and (len(data1['Name']) <= 0))):
           output_str += ",Name is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           name = data1['Name']

        if((data1.get('Mobile') is None) or ((data1.get('Mobile') is not  None) and (len(data1['Mobile']) <= 0))):
           output_str += ",Mobile is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           mobile = data1['Mobile']

        if((data1.get('Email') is None) or ((data1.get('Email') is not  None) and (len(data1['Email']) <= 0))):
           output_str += ",Email is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           email = data1['Email']

        if((data1.get('Org_Type') is None) or ((data1.get('Org_Type') is not  None) and (len(data1['Org_Type']) <= 0))):
           output_str += ",Org_Type  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           orgtype  = data1['Org_Type']
        
        if((data1.get('Country') is None) or ((data1.get('Country') is not  None) and (len(data1['Country']) <= 0))):
           output_str += ",Country  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           country  = data1['Country']


        if((data1.get('Address') is None) or ((data1.get('Address') is not  None) and (len(data1['Address']) <= 0))):
           output_str += ",Address  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           address  = data1['Address']
        
        if((data1.get('Org_Name') is None) or ((data1.get('Org_Name') is not  None) and (len(data1['Org_Name']) <= 0))):
           output_str += ",Org_Name  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           orgname  = data1['Org_Name']

        #get the status from DB

        check_rec = Light_Users.objects.filter(Username=username,Password=password)
        print "hello" 
        if(len(check_rec)>0): #just update
          
           output = '{"error_code":"4", "error_desc": "Response= Your Uername is alreay exists Please change."}'
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        otype=Light_Org_Types.objects.get(OrgTypeId=orgtype)
        oname=Light_Orgs.objects.get(OrgId=orgname)
        #print otype
        #print oname
        #print username,password,name,email,mobile,otype,country,address,oname 
        add_user_rec = Light_Users(Username=username,Password=password,Name=name,Email=email,Mobile=mobile,OrgTypeId=otype,Country=country,Address=address,OrgId=oname);
        print("1")
        add_user_rec.save()
        print("2")
        print(add_user_rec)
        if(len(str(add_user_rec)) > 0):
           output = '{"error_code":"0", "Response":"Successfully added the user : %s"}' %(username) 
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add the user"}'
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
     #}
            
     except Exception:
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
     
     if(data1.get('Username') is None):
        output_str += ",Username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",Passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("login:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
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
     if Light_Users.objects.filter(Username = username,Password=password).exists():
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
################################################################################
def add_premise(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_premise - Unable to Authenticate/add_premise... "
     try:
        data1 = json.loads(request.body)
       #print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_premise:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_premise:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
     logging.debug("add_premise:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''

     try:

        
     #{
        if((data1.get('premise_name') is None) or ((data1.get('premise_name') is not  None) and (len(data1['premise_name']) <= 0))):
           output_str += ",premise_name is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        else:
           pname = data1['premise_name']

        if((data1.get('org_id') is None) or ((data1.get('org_id') is not  None) and (len(data1['org_id']) <= 0))):
           output_str += ",org_id  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_premise:"+ output)
           return HttpResponse(output)
        else:
           orgname  = data1['org_id']

        #get the status from DB
        '''
        check_rec = Light_Users.objects.filter(Username=username,Password=password)
        if(len(check_rec)>0): #just update
           output = '{"error_code":"4", "error_desc": "Response= no rights to  change."}'
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        '''
        oid=Light_Orgs.objects.get(OrgId=orgname)
        add_user_rec = Light_Premises(PremiseDesc=pname,ChangeBy=username,OrgId=oid);
        #print("1")
        add_user_rec.save()
        #print("2")
        #print(add_user_rec)
        if(len(str(add_user_rec)) > 0):
           output = '{"error_code":"0", "Response":"Successfully added the premise : %s"}' %(username) 
           logging.debug("add_premise:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add the premise"}'
           logging.debug("add_premise:"+ output)
           return HttpResponse(output)
     #}
            
     except Exception:
     #{
         err_desc = 'add_premise:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_premise:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the premise"}'
         logging.debug("add_premise:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_premise:"+ output)
      return HttpResponse(output)

################################################################################
def add_space(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_space: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_space - Unable to Authenticate/add_space... "
     try:
        data1 = json.loads(request.body)
       #print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_space:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_space:"+ output)
        return HttpResponse(output)

     if(data1.get('Username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_space:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_space:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
     logging.debug("add_space:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_user:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''

     try:

        
     #{
        if((data1.get('premise_id') is None) or ((data1.get('premise_id') is not  None) and (len(data1['premise_id']) <= 0))):
           output_str += ",premise_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_space:"+ output)
           return HttpResponse(output)
        else:
           pid = data1['premise_id']

        if((data1.get('space_name') is None) or ((data1.get('space_name') is not  None) and (len(data1['space_name']) <= 0))):
           output_str += ",space_name  is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_space:"+ output)
           return HttpResponse(output)
        else:
           sname  = data1['space_name']

        #get the status from DB
        '''
        check_rec = Light_Users.objects.filter(Username=username,Password=password)
        if(len(check_rec)>0): #just update
           output = '{"error_code":"4", "error_desc": "Response= no rights to  change."}'
           logging.debug("add_user:"+ output)
           return HttpResponse(output)
        '''
        poid=Light_Premises.objects.get(PremiseId=pid)
        add_space_rec = Light_Spaces(SpaceDesc=sname,ChangeBy=username,PremiseId=poid);
        #print("1")
        add_space_rec.save()
        #print("2")
        #print(add_user_rec)
        if(len(str(add_space_rec)) > 0):
           output = '{"error_code":"0", "Response":"Successfully added the space : %s"}' %(username) 
           logging.debug("add_space:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add the space"}'
           logging.debug("add_space:"+ output)
           return HttpResponse(output)
     #}
            
     except Exception:
     #{
         err_desc = 'add_space:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_space:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the space"}'
         logging.debug("add_space:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_space: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_space:"+ output)
      return HttpResponse(output)

################################################################
def get_premise(request):  # this will user acces group


   if(request.method == "POST"):
   #{
     logging.debug("get_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_premise- Unable to Authenticate/get_premise... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", all details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
     logging.debug("get_premise:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''

     try:
     #{
	kwgrs={}

        if((data1.get('org_id') is None) or ((data1.get('org_id') is not  None) and (len(data1['org_id']) <= 0))):
           output_str += ",org_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        else:
           oid = data1['org_id']
        
        #Get the Curent_Status records
        curr_setting_recs = Light_Premises.objects.filter(OrgId=oid)
        #print(curr_setting_recs)
        if(curr_setting_recs > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d premises ", \n "get_premises":' %len(curr_setting_recs)
           output += '['
           counter = 0
           for rec in curr_setting_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"premise_id":"%s","premise_name":"%s"}' %(rec.PremiseId,rec.PremiseDesc)
              else:
                output += ',\n {"premise_id":"%s","premise_name":"%s"}' %(rec.PremiseId,rec.PremiseDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the premises, NO_DATA_FOUND"}'

           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
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

################################################################
def get_spaces(request):  # this will user acces group


   if(request.method == "POST"):
   #{
     logging.debug("get_premise: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_premise- Unable to Authenticate/get_premise... "
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(not data1):
        output_str += ", all details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     if(data1.get('Password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:"+ output)
        return HttpResponse(output)

     username    = data1['Username']
     password    = data1['Password']
     logging.debug("get_premise:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented)
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_premise:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''

     try:
     #{
	kwgrs={}

        if((data1.get('premise_id') is None) or ((data1.get('premise_id') is not  None) and (len(data1['premise_id']) <= 0))):
           output_str += ",premise_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        else:
           pid = data1['premise_id']
        
        #Get the Curent_Status records
        curr_setting_recs = Light_Spaces.objects.filter(PremiseId=pid)
        #print(curr_setting_recs)
        if(curr_setting_recs > 0):
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d spaces ", \n "get_spaces":' %len(curr_setting_recs)
           output += '['
           counter = 0
           for rec in curr_setting_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"space_id":"%s","space_name":"%s"}' %(rec.SpaceId,rec.SpaceDesc)
              else:
                output += ',\n {"space_id":"%s","space_name":"%s"}' %(rec.SpaceId,rec.SpaceDesc)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the premises, NO_DATA_FOUND"}'

           logging.debug("get_premise:"+ output)
           return HttpResponse(output)
     #}
     except Exception:
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


