# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import web
from web import ctx
from HarvestApp.models import *
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
################################################################################
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
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_user:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
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
     date1 = datetime.today()
     todaytime = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')     
   
     try:
     #{
        save_user = Login_Users(Uname=username,Pass=password,ChangeDate=todaytime);
        save_user.save()
        if save_user > 0:  
           output = '{"error_code":"0", "error_desc": "Response=Successfully added the User = %s"}' %(username)
           logging.debug("add_user:"+ output)
           return HttpResponse(output) 
     #}
     except Exception, e:
     #{
         err_desc = 'add_user:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_user:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the Status"}' 
         logging.debug("add_user:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_user: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_user:"+ output)
      return HttpResponse(output)





################################################################################

def add_curr_status(request):  #this will add/update the status

   if(request.method == "POST"):
   #{
     logging.debug("add_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_curr_status- Unable to Authenticate/add_curr_status... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_curr_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Tower status details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_curr_status:"+ output)
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
     logging.debug("add_curr_status:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_curr_status:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
     check_login_authenticate=False

     try:
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           check_login_authenticate=True
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)

        if((data1.get('TowerId') is None) or ((data1.get('TowerId') is not  None) and (len(data1['TowerId']) <= 0))):
           output_str += ", TowerId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           towerid = data1['TowerId']   

        if((data1.get('Status') is None) or ((data1.get('Status') is not  None) and (len(data1['Status']) <= 0))):
           output_str += ",Status is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           status = data1['Status']  
        if((data1.get('Operation') is None) or ((data1.get('Operation') is not  None) and (len(data1['Operation']) <= 0))):
           output_str += ",Operation is mandatory like ON/OFF/Started"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           operate = data1['Operation']
        if((data1.get('MachineType') is None) or ((data1.get('MachineType') is not  None) and (len(data1['MachineType']) <= 0))):
           output_str += ",Operation is mandatory "
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           mtype = data1['MachineType']
        if((data1.get('longitude') is None) or ((data1.get('longitude') is not  None) and (len(data1['longitude']) <= 0))):
           output_str += ",longitude is mandatory "
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           longitude = data1['longitude']
        if((data1.get('latitude') is None) or ((data1.get('latitude') is not  None) and (len(data1['latitude']) <= 0))):
           output_str += ",latitude is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           latitude = data1['latitude']

	'''
	if(towerid == '1' && status == '1'):
	 #engine on
	   url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
   
	
	if(towerid == '1' && status == '0'):
	# eng off
	   url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
	if(towerid == '2' && status == '1'):
	#cutting stred
	   url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)

	if(towerid == '2' && status == '0'):
	#cut done
           url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)

	if(towerid == '3' && status == '1'):
	#load str
	   url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)

	if(towerid == '3' && status == '0'):
	# load done
	   url = ''
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
 
        
        if(status == '1'):
           url = 'https://api.textlocal.in/send?username=info@gurus4geeks.com&hash=b8b15110d1e590fd94cf4347c9f2a12fbc0d6484f5115cd257297cf508b650b8&sender=JTSIOT&numbers=8897686878&message=Alert!%20Please%20check%20the%20circuit,%20as%20it%20has%20been%20tampered.%20Tower%20id:%20'+ '%s' %(towerid)
           #url = 'https://api.ipify.org/?format=json'
           #url = 'https://api.textlocal.in/send?username=info@gurus4geeks.com&hash=b8b15110d1e590fd94cf4347c9f2a12fbc0d6484f5115cd257297cf508b650b8&sender=JTSIOT&numbers=8464829792&message=Alert!%20Please%20check%20the%20circuit,%20as%20it%20has%20been%20tampered.'
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
           #return HttpResponse(data)
        
        if(status == '-1'):
           #url = 'https://api.ipify.org/?format=json'
           url = 'https://api.textlocal.in/send?username=info@gurus4geeks.com&hash=b8b15110d1e590fd94cf4347c9f2a12fbc0d6484f5115cd257297cf508b650b8&sender=JTSIOT&numbers=8897686878&message=Alert:%20Device%20disconneted%20for%20Tower%20Id%20:%20'+ '%s' %(towerid)
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
           #return HttpResponse(data)
        ''' 
        #get the status from DB
        is_history_rec_needed = True

        curr_status_recs_get = Current_Status.objects.filter(TowerId=towerid, Status=status,ChangeBy=username)
        if(len(curr_status_recs_get) > 0): #just update the ChangeDate         
           is_history_rec_needed = False
           print "rec there"
           
        
        #Add the Curent_Status record
        curr_status_rec = Current_Status(TowerId=towerid, Status=status,ChangeBy=username,Operate=operate,longitude=longitude,latitude=latitude);
        curr_status_rec.save()
        if(len(str(curr_status_rec.ChangeDate)) > 0): #If there is an exception, it will not come here
        #{
           
           #{
           curr_status_hist_rec = Current_Status_History(TowerId=towerid, Status=status,ChangeBy=username,MachineType=mtype);
           curr_status_hist_rec.save()
           if(curr_status_hist_rec.ActivityId > 0):
              date1 = datetime.today()
              curr_status_recs_get1 = Sub_Machines.objects.filter(TowerId=towerid,MachineType=mtype,ChangeBy=username)
              if(len(curr_status_recs_get1) > 0):
	         update = Sub_Machines.objects.filter(TowerId=towerid,MachineType=mtype,ChangeBy=username).update(Operate=operate,Status=status,ChangeDate=date1)
                 output = '{"error_code":"0", "error_desc": "Response=Successfully updated, Status=%s"}' %(curr_status_rec.Status)
                 logging.debug("add_curr_status:"+ output)
                 return HttpResponse(output)
              else:
                 insert = Sub_Machines(TowerId=towerid,MachineType=mtype,ChangeBy=username,Operate=operate,Status=status)
                 insert.save()
                 output = '{"error_code":"0", "error_desc": "Response=Successfully added, Status=%s"}' %(curr_status_rec.Status)
                 logging.debug("add_curr_status:"+ output)
                 return HttpResponse(output)
           else:
              output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status History"}' 
              logging.debug("add_curr_status:"+ output)
              return HttpResponse(output)
              
           #}
           '''
           else:
               output = '{"error_code":"0", "error_desc": "Response=Successfully added the Current_Status, Status=%s"}' %(curr_status_rec.Status)
               logging.debug("add_curr_status:"+ output)
               return HttpResponse(output)
           '''
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status"}' 
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'add_curr_status:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_curr_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the Status"}' 
         logging.debug("add_curr_status:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      print "this is get method"
      #lte = request.GET['hello']      
      #lte1 = request.GET['vol']
      #print lte,lte1
      #if((request.GET['hello'] is None) or ((request.GET['hello'] is not  None) and (len(request.GET['hello']) <= 0))):
      try:
         if request.method == 'GET' and 'TowerId' in request.GET:
            towerid = request.GET['TowerId']
         else:
            output_str = "TowerId is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)
         
         if request.method == 'GET' and 'MachineType' in request.GET:
            mtype = request.GET['MachineType']
         else:
            output_str = "MachineType is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)

         if request.method == 'GET' and 'Status' in request.GET:
            status = request.GET['Status']
         else:
            output_str = "Status is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)

         if request.method == 'GET' and 'Operation' in request.GET:
            operate = request.GET['Operation']
         else:
            output_str = "Operation is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)

         if request.method == 'GET' and 'longitude' in request.GET:
            longitude = request.GET['longitude']
         else:
            output_str = "longitude is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)
          
         if request.method == 'GET' and 'latitude' in request.GET:
            latitude = request.GET['latitude']
         else:
            output_str = "latitude is mandatory "
            output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
            logging.debug("add_curr_status:"+ output)
            return HttpResponse(output)
        
         is_history_rec_needed = True
         username="harvest" 
         curr_status_recs_get = Current_Status.objects.filter(TowerId=towerid, Status=status,ChangeBy=username)
         if(len(curr_status_recs_get) > 0): #just update the ChangeDate         
            is_history_rec_needed = False
            print "rec there"
                  
        
         #Add the Curent_Status record
         curr_status_rec = Current_Status(TowerId=towerid, Status=status,ChangeBy=username,Operate=operate,longitude=longitude,latitude=latitude);
         curr_status_rec.save()
         if(len(str(curr_status_rec.ChangeDate)) > 0): #If there is an exception, it will not come here
        #{
           
           #{
           curr_status_hist_rec = Current_Status_History(TowerId=towerid, Status=status,ChangeBy=username,MachineType=mtype);
           curr_status_hist_rec.save()
           if(curr_status_hist_rec.ActivityId > 0):
              date1 = datetime.today()
              curr_status_recs_get1 = Sub_Machines.objects.filter(TowerId=towerid,MachineType=mtype,ChangeBy=username)
              if(len(curr_status_recs_get1) > 0):
	         update = Sub_Machines.objects.filter(TowerId=towerid,MachineType=mtype,ChangeBy=username).update(Operate=operate,Status=status,ChangeDate=date1)
                 output = '{"error_code":"0", "error_desc": "Response=Successfully updated, Status=%s"}' %(curr_status_rec.Status)
                 logging.debug("add_curr_status:"+ output)
                 return HttpResponse(output)
              else:
                 insert = Sub_Machines(TowerId=towerid,MachineType=mtype,ChangeBy=username,Operate=operate,Status=status)
                 insert.save()
                 output = '{"error_code":"0", "error_desc": "Response=Successfully added, Status=%s"}' %(curr_status_rec.Status)
                 logging.debug("add_curr_status:"+ output)
                 return HttpResponse(output)
           else:
              output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status History"}' 
              logging.debug("add_curr_status:"+ output)
              return HttpResponse(output)
              
           #}

                        
         
      except ValueError:
         return HttpResponse("error")
      #logging.debug("add_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      #output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      #logging.debug("add_curr_status:"+ output)
      #return HttpResponse(l1)

################################################################################
def del_curr_status(request):  #this will del the status

   if(request.method == "POST"):
   #{
     logging.debug("del_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "del_curr_status- Unable to Authenticate/add_curr_status... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_curr_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Tower status details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_curr_status:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_curr_status:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_curr_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("del_curr_status:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("del_curr_status:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        if((data1.get('TowerId') is None) or ((data1.get('TowerId') is not  None) and (len(data1['TowerId']) <= 0))):
           output_str += ", TowerId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("del_curr_status:"+ output)
           return HttpResponse(output)
        else:
           towerid = data1['TowerId']   
        '''
        if((data1.get('Status') is None) or ((data1.get('Status') is not  None) and (len(data1['Status']) <= 0))):
           output_str += ",Status is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_curr_status:"+ output)
           return HttpResponse(output)
        else:
           status = data1['Status']   
        '''
        #get the status from DB
        is_history_rec_needed = True

        curr_status_recs_get = Current_Status.objects.filter(TowerId=towerid)
        if(len(curr_status_recs_get) > 0): #just update the ChangeDate         
           is_history_rec_needed = False
           
        
        #Add the Curent_Status record
        curr_status_rec = Current_Status(TowerId=towerid,ChangeBy=username);
        curr_status_rec.delete()
        if(len(str(curr_status_rec.ChangeDate)) > 0): #If there is an exception, it will not come here
        #{
           if(is_history_rec_needed == True):
           #{
              curr_status_hist_rec = Current_Status_History(TowerId=towerid,ChangeBy=username);
              curr_status_hist_rec.delete()
              if(curr_status_hist_rec.ActivityId > 0):
                 output = '{"error_code":"0", "error_desc": "Response=Successfully deleteed the TowerId=%s"}' %(curr_status_rec.TowerId)
                 logging.debug("del_curr_status:"+ output)
                 return HttpResponse(output)
              else:
                 output = '{"error_code":"3", "error_desc": "Response=Failed to del towerid  History"}' 
                 logging.debug("del_curr_status:"+ output)
                 return HttpResponse(output)
           #}
           else:
               output = '{"error_code":"0", "error_desc": "Response=Successfully delete TowerId :=%s"}' %(towerid)
               logging.debug("del_curr_status:"+ output)
               return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status"}' 
           logging.debug("del_curr_status:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'del_curr_status:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("del_curr_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the Status"}' 
         logging.debug("del_curr_status:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("del_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("del_curr_status:"+ output)
      return HttpResponse(output)


################################################################################
def get_curr_status(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_curr_status- Unable to Authenticate/get_curr_status... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_curr_status:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     '''
     check_login_authenticate=False
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)


        towerid = ""   
        status = ""
        uname=""
        kwargs = {}
        
        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        if((data1.get('Status') is not  None) and (len(data1['Status']) > 0)):
           status = data1['Status']   
           kwargs['Status'] = status
        '''
        if((data1.get('username') is not  None) and (len(data1['username']) > 0)):
           uname = data1['username']   
           kwargs['username'] = uname
        '''
        #uname = data1['username']
        #kwargs['username'] = uname   
        #Get the Curent_Status records
        print("aray data",kwargs)
        curr_status_recs = Current_Status.objects.filter(ChangeBy=username,**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           print("in")
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d Current_Status recs", \n "current_status_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"TowerId":"%s", "Status":"%s", "ChangeDate":"%s","Operate":"%s"}' %(rec.TowerId, rec.Status, rec.ChangeDate,rec.Operate)
              else: 
                output += ',\n {"TowerId":"%s", "Status":"%s", "ChangeDate":"%s","Operate":"%s"}' %(rec.TowerId, rec.Status, rec.ChangeDate,rec.Operate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_curr_status:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status records, NO_DATA_FOUND"}' 
           logging.debug("get_curr_status:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_curr_status:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_curr_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the Status"}' 
         logging.debug("get_curr_status:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_curr_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_curr_status:"+ output)
      return HttpResponse(output)


################################################################################

def get_curr_status_history(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_curr_status_history: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_curr_status_history- Unable to Authenticate/get_curr_status_history... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status_history:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status_history:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_history:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_history:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_curr_status_history:input: user="+username)
     '''	
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_history:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
   
     try:
     #{

        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        towerid = ""   
        status = ""
        DTR_Week  = False
        DTR_Month = False
        DTR_Year  = False
        DTR_Today = False
        

        curr_date = time.strftime('%Y-%m-%d')
        kwargs = {}

        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        if((data1.get('Status') is not  None) and (len(data1['Status']) > 0)):
           status = data1['Status']   
           kwargs['Status'] = status

        if((data1.get('DTR_Week') is not  None) and (len(data1['DTR_Week']) > 0) and (data1['DTR_Week'].upper() == 'YES')):
           DTR_Week = True 

        if((data1.get('DTR_Month') is not  None) and (len(data1['DTR_Month']) > 0) and (data1['DTR_Month'].upper() == 'YES')):
           DTR_Month = True

        if((data1.get('DTR_Year') is not  None) and (len(data1['DTR_Year']) > 0) and (data1['DTR_Year'].upper() == 'YES')):
           DTR_Year = True

        if((data1.get('DTR_Today') is not  None) and (len(data1['DTR_Today']) > 0) and (data1['DTR_Today'].upper() == 'YES')):
           DTR_Today = True

        #Get the Curent_Status History records
        output = ""

        if((DTR_Week == False) and (DTR_Month == False) and (DTR_Year == False)) or (DTR_Today == True):
        #{ 
           today = dt1.date.today()
           kwargs['ChangeDate__gte'] = today
           curr_status_recs = Current_Status_History.objects.filter(ChangeBy=username,**kwargs)
           output = '{"error_code":"0", "error_desc": "Response=Current_Status history recs"' 
           output += ',\n "current_status_hist_details_today":['
           if(len(curr_status_recs) > 0): 
           #{
              counter = 0
              for rec in curr_status_recs:
              #{
                 counter += 1
                 if(counter == 1):
                   output += '{"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
                 else: 
                   output += ',\n {"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
              #}
              output += ']\n'
              #output += '}'
              #cust_recs_json = serializers.serialize("json", curr_status_recs)
              #logging.debug("get_curr_status_history:"+ output)
           #}
           else:
              output += ']\n'
              output1 = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status records, NO_DATA_FOUND"}' 
              logging.debug("get_curr_status_history:"+ output1)
              #return HttpResponse(output)
        #} 
       
        if(DTR_Week == True):
        #{
           current_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
           last_n_days=7
           kwargs['ChangeDate__gte'] = current_time - dt1.timedelta(0, int(last_n_days*24*60*60))

           curr_status_recs = Current_Status_History.objects.filter(**kwargs)
           if(len(output)<= 10): 
              output = '{"error_code":"0", "error_desc": "Response=Current_Status history recs"' 
           output += ',\n "current_status_hist_details_week":['

           if(len(curr_status_recs) > 0): 
           #{
              counter = 0
              for rec in curr_status_recs:
              #{
                 counter += 1
                 if(counter == 1):
                   output += '{"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
                 else: 
                   output += ',\n {"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
              #}
              output += ']\n'
           #}
           else:
              output += ']\n'
              output1 = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status records, NO_DATA_FOUND"}' 
              logging.debug("get_curr_status_history:"+ output1)
              #return HttpResponse(output)
        #}

        if(DTR_Month == True):
        #{
           today = dt1.date.today()
           curr_day=today.day
           first = today.replace(day=1) #first day of the current month
           lastMonth = first - dt1.timedelta(days=1) #end of the previous month
           month_old_date = '%s-%s-%s' %(lastMonth.year, lastMonth.month, curr_day)
           kwargs['ChangeDate__gte'] = month_old_date

           curr_status_recs = Current_Status_History.objects.filter(ChangeBy=username,**kwargs)
           if(len(output)<= 10): 
              output = '{"error_code":"0", "error_desc": "Response=Current_Status history recs"' 
           output += ',\n "current_status_hist_details_month":['

           if(len(curr_status_recs) > 0): 
           #{
              counter = 0
              for rec in curr_status_recs:
              #{
                 counter += 1
                 if(counter == 1):
                   output += '{"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
                 else: 
                   output += ',\n {"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
              #}
              output += ']\n'
           #}
           else:
              output += ']\n'
              output1 = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status records, NO_DATA_FOUND"}' 
              logging.debug("get_curr_status_history:"+ output1)
              #return HttpResponse(output)
        #}
        if(DTR_Year == True):
        #{
           today = dt1.date.today()
           year_old_date = '%s-%s-%s' %(today.year -1 , today.month, today.day)
           kwargs['ChangeDate__gte'] = year_old_date

           curr_status_recs = Current_Status_History.objects.filter(**kwargs)
           if(len(output)<= 10): 
              output = '{"error_code":"0", "error_desc": "Response=Current_Status history recs"' 
           output += ',\n "current_status_hist_details_year":['

           if(len(curr_status_recs) > 0): 
           #{
              counter = 0
              for rec in curr_status_recs:
              #{
                 counter += 1
                 if(counter == 1):
                   output += '{"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
                 else: 
                   output += ',\n {"ActivityId":"%s","TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.ActivityId, rec.TowerId, rec.Status, rec.ChangeDate)
              #}
              output += ']\n'
           #}
           else:
              output += ']\n'
              output1 = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status records, NO_DATA_FOUND"}' 
              logging.debug("get_curr_status_history:"+ output1)
              #return HttpResponse(output)
        #}
        output += '}'
        #cust_recs_json = serializers.serialize("json", curr_status_recs)
        logging.debug("get_curr_status_history:"+ output)
        return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_curr_status_history:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_curr_status_history:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the Status history "}' 
         logging.debug("get_curr_status_history:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_curr_status_history: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_curr_status_history:"+ output)
      return HttpResponse(output)
#################################################################################
def get_excelSheet(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_excel_history: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_excel_history- Unable to Authenticate/get_excel_history... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_excel_history:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_excel_history:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excel_history:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excel_history:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_excel_history:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excel_history:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
   
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        towerid = ""   
        status = ""
        

        curr_date = time.strftime('%Y-%m-%d')
        kwargs = {}

        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid
       
          
	if(data1.get('StartDate') is None):
           output_str += ",StartDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_excel:"+ output)
           return HttpResponse(output)

        if(data1.get('EndDate') is None):
           output_str += ",EndDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_excel:"+ output)
           return HttpResponse(output)
	start_date  = data1['StartDate']
     	end_date    = data1['EndDate']
	
	start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        curr_status_recs = Current_Status_History.objects.filter(ChangeBy=username,TowerId=towerid,ChangeDate__range=[start_date, end_date])
#	curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=[start_date, end_date]).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]
        #Get the Curent_Status records
        #curr_status_recs = Current_Status_History.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0):
           #print("enter recs") 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d Startdate recs", \n "StartDate_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              #print("in for")
              counter += 1
              if(counter == 1):
                #print("in count")
                output += '{"TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.TowerId, rec.Status, rec.ChangeDate) 
              else: 
   		#print("in count else")
                output += ',\n {"TowerId":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.TowerId, rec.Status,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_StartDate:"+ output)
           return HttpResponse(output)
        #}
        else:
           #print("in else")
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the StartDate records, NO_DATA_FOUND"}' 
           logging.debug("get_StartDate:"+ output)
           return HttpResponse(output)




     except Exception, e:
     #{
         err_desc = 'get_excel_history:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_excel_history:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the excel history "}' 
         logging.debug("get_excel_history:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_excel_history: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_excel_history:"+ output)
      return HttpResponse(output)
#



################################################################################
def get_top_violators(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_top_violators: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_top_violators- Unable to Authenticate/get_top_violators... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)

     if(data1.get('Start_Date') is None):
        output_str += ",Start_Date is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)

     if(data1.get('End_Date') is None):
        output_str += ",End_Date is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_top_violators:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     start_date  = data1['Start_Date']
     end_date    = data1['End_Date']
     logging.debug("get_top_violators:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_top_violators:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
   
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        kwargs = {}

        #Get the Curent_Status records
        #curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=['%s', '%s']).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count').filter(valve_open_count__in=top_valve_open_count[:10]) %(start_date, end_date)
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        curr_status_hist_recs = Current_Status_History.objects.filter(ChangeBy=username,Status=1, ChangeDate__range=[start_date, end_date]).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]  
        #curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=['2017-03-01', '2017-09-07']).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]
        if(len(curr_status_hist_recs) > 0): 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got violators recs", \n "violators_details":' 
           output += '['
           counter = 0
           for rec in curr_status_hist_recs:
           #{
              counter += 1
              #logging.debug(type(rec))
              db_TowerId = ""
              db_valve_open_count = ""

              for k,v in rec.items():
                 if(k == "TowerId"):
                    db_TowerId = v
                 elif(k == "valve_open_count"):
                    db_valve_open_count = v 

              if(counter == 1):
                output += '{"TowerId":"%s", "Valve_Open_Count":"%s"}' %(db_TowerId, db_valve_open_count)
              else: 
                output += ',\n {"TowerId":"%s", "Valve_Open_Count":"%s"}' %(db_TowerId, db_valve_open_count)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_hist_recs)
           logging.debug("get_top_violators:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the Current_Status Hist records, NO_DATA_FOUND"}' 
           logging.debug("get_top_violators:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_top_violators:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_top_violators:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the top violators"}' 
         logging.debug("get_top_violators:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_top_violators: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_top_violators:"+ output)
      return HttpResponse(output)
##############################################################################
def send_messege(request):  #this will send messege status to number

   if(request.method == "POST"):
   #{
     logging.debug("send_messege: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "send_messege - Unable to Authenticate/send_messege... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("del_curr_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", All details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("send_messege:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("send_messege:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("send_messege:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("send_messege:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("send_messege:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
        
      
       
        if((data1.get('TowerId') is None) or ((data1.get('TowerId') is not  None) and (len(data1['TowerId']) <= 0))):
           output_str += ", TowerId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("send_messege:"+ output)
           return HttpResponse(output)
        else:
           towerid = data1['TowerId']   
           #print("this is thowerid")
       
        if((data1.get('Status') is None) or ((data1.get('Status') is not  None) and (len(data1['Status']) <= 0))):
           output_str += ",Status is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("send_messege:"+ output)
           return HttpResponse(output)
        else:
           status = data1['Status']
           #print(status) 
        if(status == '-1'):
           #url = 'https://api.ipify.org/?format=json'
           url = 'https://api.textlocal.in/send?username=info@gurus4geeks.com&hash=b8b15110d1e590fd94cf4347c9f2a12fbc0d6484f5115cd257297cf508b650b8&sender=JTSIOT&numbers=8464829792&message=Alert!%20Please%20check%20the%20circuit,%20as%20it%20has%20been%20tampered.'
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
           return HttpResponse(data)

        if(status == '-2'):
           #url = 'https://api.ipify.org/?format=json'
           url = 'https://api.textlocal.in/send?username=info@gurus4geeks.com&hash=b8b15110d1e590fd94cf4347c9f2a12fbc0d6484f5115cd257297cf508b650b8&sender=JTSIOT&numbers=8464829792&message=Alert!%20Please%20check%20the%20circuit,%20as%20it%20has%20been%20tampered.'
           serialized_data = urllib2.urlopen(url).read()
           data = json.loads(serialized_data)
           print(data)
           return HttpResponse(data)



  
        ''' 
        #get the status from DB
        is_history_rec_needed = True

        curr_status_recs_get = Current_Status.objects.filter(TowerId=towerid)
        if(len(curr_status_recs_get) > 0): #just update the ChangeDate         
           is_history_rec_needed = False
           
        
        #Add the Curent_Status record
        curr_status_rec = Current_Status(TowerId=towerid);
        curr_status_rec.delete()
        if(len(str(curr_status_rec.ChangeDate)) > 0): #If there is an exception, it will not come here
        #{
           if(is_history_rec_needed == True):
           #{
              curr_status_hist_rec = Current_Status_History(TowerId=towerid);
              curr_status_hist_rec.delete()
              if(curr_status_hist_rec.ActivityId > 0):
                 output = '{"error_code":"0", "error_desc": "Response=Successfully deleteed the TowerId=%s"}' %(curr_status_rec.TowerId)
                 logging.debug("del_curr_status:"+ output)
                 return HttpResponse(output)
              else:
                 output = '{"error_code":"3", "error_desc": "Response=Failed to del towerid  History"}' 
                 logging.debug("del_curr_status:"+ output)
                 return HttpResponse(output)
           #}
           else:
               output = '{"error_code":"0", "error_desc": "Response=Successfully delete TowerId :=%s"}' %(towerid)
               logging.debug("del_curr_status:"+ output)
               return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add Current Status"}' 
           logging.debug("del_curr_status:"+ output)
           return HttpResponse(output)
        '''
     #}
     except Exception, e:
     #{
         err_desc = 'send_messege:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("send_messege:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to send messege"}' 
         logging.debug("send_messege:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("send_messege: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("send_messege:"+ output)
      return HttpResponse(output)


################################################################################
###########################
def get_machine_location(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_machine_location: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_machine_location:- Unable to Authenticate/get_machine_location... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_machine_location:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_machine_location:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_machine_location:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_machine_location:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_machine_location:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_machine_location:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     '''
     check_login_authenticate=False
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_machine_location:Failed to Authenticate"+ output)
          return HttpResponse(output)


        towerid = ""   
        status = ""
        uname=""
        kwargs = {}
        
        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        
        '''
        if((data1.get('username') is not  None) and (len(data1['username']) > 0)):
           uname = data1['username']   
           kwargs['username'] = uname
        '''
        #uname = data1['username']
        #kwargs['username'] = uname   
        #Get the Curent_Status records
        print("aray data",kwargs)
        curr_status_recs = Current_Status.objects.filter(ChangeBy=username,**kwargs)
        if(len(curr_status_recs) > 0): 
        #{
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d machines", \n "machine_loc_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              counter += 1
              if(counter == 1):
                output += '{"machine_id":"%s", "longitude":"%s", "latitude":"%s"}' %(rec.TowerId, rec.longitude, rec.latitude)
              else: 
                output += ',\n {"machine_id":"%s", "longitude":"%s", "latitude":"%s"}' %(rec.TowerId, rec.longitude, rec.latitude)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_machine_location:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the machine locations, NO_DATA_FOUND"}' 
           logging.debug("get_machine_location:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_machine_location:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_machine_location:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the machine locations"}' 
         logging.debug("get_machine_location:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_machine_location: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_machine_location:"+ output)
      return HttpResponse(output)

#################################
def get_excelSheet1(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_excelSheet1: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_excelSheet1- Unable to Authenticate/get_excelSheet1... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_excelSheet1:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_excelSheet1:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excelSheet1:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excelSheet1:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_excelSheet1:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_excelSheet1:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
   
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        towerid = ""   
        mtype = ""
        

        curr_date = time.strftime('%Y-%m-%d')
        kwargs = {}

        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid

        if((data1.get('MachineType') is not  None) and (len(data1['MachineType']) > 0)):
           mtype = data1['MachineType']   
           kwargs['MachineType'] = mtype
       
          
	if(data1.get('StartDate') is None):
           output_str += ",StartDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_excelSheet1:"+ output)
           return HttpResponse(output)

        if(data1.get('EndDate') is None):
           output_str += ",EndDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_excelSheet1:"+ output)
           return HttpResponse(output)
	start_date  = data1['StartDate']
     	end_date    = data1['EndDate']
	
	start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        curr_status_recs = Current_Status_History.objects.filter(ChangeBy=username,ChangeDate__range=[start_date, end_date],**kwargs)
#	curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=[start_date, end_date]).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]
        #Get the Curent_Status records
        #curr_status_recs = Current_Status_History.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0):
           #print("enter recs") 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d Startdate recs", \n "StartDate_details":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              #print("in for")
              counter += 1
              if(counter == 1):
                #print("in count")
                output += '{"TowerId":"%s", "MachineType":"%s", "Status":"%s", "ChangeDate":"%s"}' %(rec.TowerId, rec.MachineType, rec.Status, rec.ChangeDate) 
              else: 
   		#print("in count else")
                output += ',\n {"TowerId":"%s", "MachineType":"%s","Status":"%s", "ChangeDate":"%s"}' %(rec.TowerId, rec.MachineType,rec.Status,rec.ChangeDate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_excelSheet1:"+ output)
           return HttpResponse(output)
        #}
        else:
           #print("in else")
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the StartDate records, NO_DATA_FOUND"}' 
           logging.debug("get_excelSheet1:"+ output)
           return HttpResponse(output)




     except Exception, e:
     #{
         err_desc = 'get_excelSheet1:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_excelSheet1:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the excel history "}' 
         logging.debug("get_excelSheet1:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_excelSheet1: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_excelSheet1:"+ output)
      return HttpResponse(output)

#################################
def get_curr_status_sub(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_curr_status_sub: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_curr_status_sub- Unable to Authenticate/get_curr_status_sub... " 
     try:
        data1 = json.loads(request.body)
        print(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status_sub:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Login details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_curr_status_sub:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_sub:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_sub:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_curr_status_sub:input: user="+username)
     '''
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_curr_status_sub:Failed to Authenticate"+ output)
        return HttpResponse(output)
     '''  
   
     try:
     #{
        if Login_Users.objects.filter(Uname = username,Pass=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_curr_status:Failed to Authenticate"+ output)
          return HttpResponse(output)
        towerid = ""   
        mtype = ""
        

        curr_date = time.strftime('%Y-%m-%d')
        kwargs = {}

        if((data1.get('TowerId') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid
        
        
        curr_status_recs = Sub_Machines.objects.filter(ChangeBy=username,**kwargs)
#	curr_status_hist_recs = Current_Status_History.objects.filter(Status=1, ChangeDate__range=[start_date, end_date]).values('TowerId').annotate(valve_open_count=Count('Status')).order_by('-valve_open_count')[:10]
        #Get the Curent_Status records
        #curr_status_recs = Current_Status_History.objects.filter(**kwargs)
        if(len(curr_status_recs) > 0):
           #print("enter recs") 
        #{
           output = '{"error_code":"0", "error_desc": "Response=Successfully got %d current status recs", \n "current_status_details_sup":' %len(curr_status_recs)
           output += '['
           counter = 0
           for rec in curr_status_recs:
           #{
              #print("in for")
              counter += 1
              if(counter == 1):
                #print("in count")
                output += '{"TowerId":"%s", "MachineType":"%s", "Status":"%s", "ChangeDate":"%s","Operate":"%s"}' %(rec.TowerId, rec.MachineType, rec.Status, rec.ChangeDate,rec.Operate) 
              else: 
   		#print("in count else")
                output += ',\n {"TowerId":"%s", "MachineType":"%s","Status":"%s", "ChangeDate":"%s","Operate":"%s"}' %(rec.TowerId, rec.MachineType,rec.Status,rec.ChangeDate,rec.Operate)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_curr_status_sub:"+ output)
           return HttpResponse(output)
        #}
        else:
           #print("in else")
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the records, NO_DATA_FOUND"}' 
           logging.debug("get_curr_status_sub:"+ output)
           return HttpResponse(output)




     except Exception, e:
     #{
         err_desc = 'get_curr_status_sub:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_curr_status_sub:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the Status "}' 
         logging.debug("get_curr_status_sub:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_curr_status_sub: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_curr_status_sub:"+ output)
      return HttpResponse(output)
