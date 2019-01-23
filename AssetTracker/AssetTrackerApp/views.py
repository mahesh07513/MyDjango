from __future__ import unicode_literals
from django.shortcuts import render
from AssetTrackerApp.models import *
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
import MySQLdb
import threading
import numpy as np
db = MySQLdb.connect("localhost","assettrack","ptlasset","AssetTracker")
cursor = db.cursor()

# Create your views here.
###############################
#def ssid_str_reset():
  
   #threading.Timer(180.0, ssid_str_reset).start()
   #Asset_SSID.objects.all().update(Str_ssid='0')
   
#ssid_str_reset()

##############################################################################
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
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        
        kwargs = {}

       
        #Get the Curent_Status records
        get_rooms_rec = Asset_Rooms.objects.filter(**kwargs)
        if(len(get_rooms_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d rooms", \n "get_rooms":' %len(get_rooms_rec)
           output += '['
           counter = 0
           for rec in get_rooms_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"room_id":"%s"}' %(rec.Room_id )
              else: 
                output += ',\n {"room_id":"%s"}' %(rec.Room_id)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_rooms:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the room records, NO_DATA_FOUND"}' 
           logging.debug("get_rooms:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_rooms:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_rooms:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the Rooms"}' 
         logging.debug("get_rooms:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_rooms: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_rooms:"+ output)
      return HttpResponse(output)
###########################################################################
def get_rooms_ssid(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_rooms_ssid - Unable to Authenticate/get_rooms_ssid... " 
     try:
        data1 = json.loads(request.body)
        print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_rooms_ssid:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms_ssid:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_rooms_ssid:input: user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_rooms_ssid:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        roomid="" 
        kwargs = {}
        status="active"
        status1="inactive"
        '''
	if((data1.get('room_id') is None) or ((data1.get('roomid') is not  None) and (len(data1['room_id']) <= 0))):
           output_str += ", room_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("get_rooms_ssid:"+ output)
           return HttpResponse(output)
        else:
           roomid = data1['room_id']
       	   #kwargs['room_id'] = roomid
       
        if((data1.get('room_id') is not  None) and (len(data1['TowerId']) > 0)):
           towerid = data1['TowerId']   
           kwargs['TowerId'] = towerid
        '''
        date1 = datetime.today()
        change_dt = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
        '''
        date1 = datetime.today()
        change_dt = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
        print(change_dt)
        list1=[]
        list2=[]
        list3=[]
        get_rooms_ssid_rec1 = Asset_Ssid_Str.objects.filter(Room_id=roomid)
        if(len(get_rooms_ssid_rec1) > 0):
           print("inside if")
           for rec in get_rooms_ssid_rec1:
              print("inside for",rec)
              add1=rec.Str_ssid
              add2=rec.Room_id.Room_id
              add3=rec.Ssid.Ssid
              print(rec.Str_ssid)
              list1.append(add1)
              list2.append(add2)
              list3.append(add3)
           minStr=list1.index(min(list1))
           print(list1)
           print(minStr)
           print(list2)
           roomname=list2[minStr]
           ssidname=list3[minStr]
           print(roomname)
           print(ssidname)
           update_rec=Asset_SSID.objects.filter(Ssid=ssidname).update(Room_id=roomname,Change_Date=change_dt)
           if(update_rec > 0):
              print("update success")

        #Get the Curent_Status records
        #get_rooms_ssid_rec = Asset_Ssid_Str.objects.filter(Room_id=roomid)
              #get_rooms_ssid_rec3 = Asset_SSID.objects.raw("SELECT * FROM Asset_SSID where Room_id=%s;") %(roomid)
        
        cursor.execute("SELECT * FROM Asset_SSID ")
        get_rooms_ssid_rec3 = cursor.fetchall()
        '''
        date1 = datetime.today()

  #present1 ="2018-01-31 13:03"

        end_date = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')

        print(end_date)
        get_rooms_ssid_rec3 = Asset_SSID.objects.all()
        if(len(get_rooms_ssid_rec3) > 0):
           output = '{"error_code":"0", "Response":"Successfully got %d ssid names", \n "get_rooms_ssid":'%len(get_rooms_ssid_rec3)
           output += '['
           counter = 0
	   for rec in get_rooms_ssid_rec3:
               time1=rec.Change_Date
               sttime=datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
               endtime=datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
               fmt = '%Y-%m-%d %H:%M:%S'
	       d1 = datetime.strptime(sttime, fmt)
	       d2 = datetime.strptime(endtime, fmt)
               timediff=int((d1-d2).total_seconds())
               status=""
               if(timediff<120):
                  status="active"
               else:
                  status="inactive"  
               counter += 1
               if(counter == 1):
                 output += '{"ssid":"%s","room_id":"%s","status":"%s"}' %(rec.Ssid ,rec.Room_id.Room_id,status)
               else: 
                   output += ',\n {"ssid":"%s","room_id":"%s","status":"%s"}' %(rec.Ssid,rec.Room_id.Room_id,status)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_rooms_ssid:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the room ssid records, NO_DATA_FOUND"}' 
           logging.debug("get_rooms_ssid:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_rooms_ssid:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_rooms_ssid:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the Room ssid"}' 
         logging.debug("get_rooms_ssid:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_rooms_ssid:"+ output)
      return HttpResponse(output)
#####################################################################
def add_rooms_ssid(request):  #this will add the ssid to rooms

   if(request.method == "POST"):
   #{
     logging.debug("add_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_rooms_ssid - Unable to Authenticate/add_rooms_ssid... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_rooms_ssid:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_curr_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("add_rooms_ssid: input user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_rooms_ssid:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        tssid = []
        if((data1.get('room_id') is None) or ((data1.get('room_id') is not  None) and (len(data1['room_id']) <= 0))):
           output_str += ", room_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_rooms_ssid:"+ output)
           return HttpResponse(output)
        else:
           roomid = data1['room_id']   
        #ssidlist={}
        if((data1.get('ssid_list') is None) or ((data1.get('ssid_list') is not  None) and (len(data1['ssid_list']) <= 0))):
           output_str += ",ssid_list is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_rooms_ssid:"+ output)
           return HttpResponse(output)
        else:
           ssidlist = data1['ssid_list']   
           #ssidlist['ssid_list']=ssid_list
        date1 = datetime.today()
        change_dt = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
        print(change_dt)
        print(ssidlist)
        slist=str(ssidlist)[1:-1]
        print str(ssidlist)[1:-1]
        print len(slist.split(","))
        if(len(slist) == 0 ):
           output_str += ",no data to add"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_rooms_ssid:"+ output)
           return HttpResponse(output)

        add_ssid_rec=False
        add_room_rec2=False
        add_room_rec3=False
        for ssid in slist.split(","):
           print(ssid)
           tssid.append(ssid)
        print(tssid) 
        #get the status from DB
        get_rooms_recs = Asset_Rooms.objects.filter(Room_id=roomid)
        if(len(get_rooms_recs) > 0): #just update the ChangeDate  
           print("data is there")       
           for ssid in tssid:
              print("inside for 2")
              print(ssid)   
              ssid=ssid.strip()
              print(roomid)
              print(change_dt)
              cursor.execute("""INSERT INTO Asset_SSID(Ssid,Change_Date,Room_id) VALUES (%s,%s,%s)""",(ssid,change_dt,roomid))
              db.commit()
              add_ssid_rec=True
              #add_ssid_rec = Asset_SSID(Ssid=ssid,Room_id=roomid,Change_Date=change_dt)
              #add_ssid_rec.save()
           if(add_ssid_rec ==True):
              output = '{"error_code":"0", "Response":"Successfully added the ssid to room : %s"}' %(roomid)
              logging.debug("add_rooms_ssid:"+ output)
              return HttpResponse(output) 
           
        else:
           print("data is not there")
           add_room_rec1 = Asset_Rooms(Room_id=roomid, Room_desc=roomid,Change_Date=change_dt);
           add_room_rec1.save()
           add_room_rec3=True
           if(add_room_rec1 > 0):
              print("data saved")
              for ssid in tssid:
                 print("inside for ")
                 #add_rec_ssid = Asset_SSID(Room_id=roomid, Ssid=ssid, Change_Date=change_dt);
                 #add_rec_ssid.save()
                 ssid=ssid.strip()
                 cursor.execute("""INSERT INTO Asset_SSID(Ssid,Change_Date,Room_id) VALUES (%s,%s,%s)""",(ssid,change_dt,roomid))
                 db.commit()
                 add_room_rec2=True

           if(add_room_rec2 == True and add_room_rec3==True):
              output = '{"error_code":"0", "Response":"Successfully added the ssid to room : %s"}' %(roomid)
              logging.debug("add_rooms_ssid:"+ output)
              return HttpResponse(output)
 
        
     #}
     except Exception, e:
     #{
         err_desc = 'add_rooms_ssid:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_rooms_ssid:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the ssid to room}' 
         logging.debug("add_rooms_ssid:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_rooms_ssid:"+ output)
      return HttpResponse(output)

########################################################################
def modify_rooms_ssid(request):  #this will add the ssid to rooms

   if(request.method == "POST"):
   #{
     logging.debug("modify_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "modify_rooms_ssid - Unable to Authenticate/modify_rooms_ssid... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("modify_rooms_ssid:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("modify_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("modify_rooms_ssid:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("modify_rooms_ssid:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("modify_rooms_ssid: input user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("modify_rooms_ssid:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        tssid = []
        if((data1.get('room_id') is None) or ((data1.get('room_id') is not  None) and (len(data1['room_id']) <= 0))):
           output_str += ", room_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("modify_rooms_ssid"+ output)
           return HttpResponse(output)
        else:
           roomid = data1['room_id']   
        #ssidlist={}
        if((data1.get('ssid') is None) or ((data1.get('ssid') is not  None) and (len(data1['ssid']) <= 0))):
           output_str += ",ssid is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("modify_rooms_ssid:"+ output)
           return HttpResponse(output)
        else:
           ssid = data1['ssid']   
           #ssidlist['ssid_list']=ssid_list
        date1 = datetime.today()
        change_dt = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
        print(change_dt)
        '''
        print(ssidlist)
        slist=str(ssidlist)[1:-1]
        print str(ssidlist)[1:-1]
        print len(slist.split(","))
        if(len(slist) == 0 ):
           output_str += ",no data to add"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_rooms_ssid:"+ output)
           return HttpResponse(output)
        '''
               
        #get the status from DB
        update_rooms_recs = Asset_Rooms.objects.filter(Ssid=ssid).update(Room_id=roomid)
        if(len(update_rooms_recs) > 0): #just update the ChangeDate  
           output = '{"error_code":"0", "Response":"Successfully ssid the ssid to room : %s"}' %(roomid)
           logging.debug(":modify_rooms_ssid"+ output)
           return HttpResponse(output) 
           
        else:
           output = '{"error_code":"2", "error_desc": "Response = failed to modify to ssid to room : %s"}' %(roomid)
           logging.debug("modify_rooms_ssid:"+ output)
           return HttpResponse(output)   
 
        
     #}
     except Exception, e:
     #{
         err_desc = 'modify_rooms_ssid:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("modify_rooms_ssid:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to modify the ssid to room}' 
         logging.debug("modify_rooms_ssid:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("modify_rooms_ssid: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("modify_rooms_ssid:"+ output)
      return HttpResponse(output)

#######################################################################
def add_ssid_status(request):  #this will add the ssid str

   if(request.method == "POST"):
   #{
     logging.debug("add_ssid_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_ssid_status - Unable to Authenticate/add_ssid_status... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_ssid_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_ssid_status:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_ssid_status:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_ssid_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("add_ssid_status: input user="+username)

     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("add_ssid_status:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
   
     try:
     #{
        tssid = []
        tstr  = []
        if((data1.get('room_id') is None) or ((data1.get('room_id') is not  None) and (len(data1['room_id']) <= 0))):
           output_str += ", room_id is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output)
        else:
           roomid = data1['room_id']   
        #ssidlist={}
        if((data1.get('ssid_list') is None) or ((data1.get('ssid_list') is not  None) and (len(data1['ssid_list']) <= 0))):
           output_str += ",ssid_list is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output)
        else:
           ssidlist = data1['ssid_list']   
        
        if((data1.get('ssid_str') is None) or ((data1.get('ssid_str') is not  None) and (len(data1['ssid_str']) <= 0))):
           output_str += ",ssid_str is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output)
        else:
           ssidstr = data1['ssid_str']


        date1 = datetime.today()
        change_dt = datetime.strftime(date1, '%Y-%m-%d %H:%M:%S')
        print(change_dt)
        print(ssidlist)
        print(ssidstr)
        sstr=str(ssidstr)[1:-1]
        slist=str(ssidlist)[1:-1]
        
        if(len(slist) == 0 or len(sstr) == 0):
           output_str += ",no data to add"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output)

        save_recs1=False
        save_recs2=False
        save_recs3=False
        for ssid in slist.split(","):
           print(ssid)
           tssid.append(ssid)
        print(tssid)
       
        for str1 in sstr.split(","):
           str1=str1.strip()
           print(str1)
           tstr.append(str1)
        print(tstr)
  	dbssid=[]
        c=[]
        cursor=db.cursor()
        cursor.execute("SELECT * FROM Asset_SSID")
        ck_room_recs1 = cursor.fetchall()
        cursor.close()
        for rec in ck_room_recs1:
           ssid2=str(rec[0])
           dbssid.append(ssid2)
        print("db data :",dbssid)   
        a = np.array(tssid)
        b = np.array(dbssid)
   	c=np.intersect1d(a,b)
	print("compare data",c)
        if(len(c)>0):
           for rec1 in c:
              print("c data",rec1) 
              cursor=db.cursor()
              cursor.execute ("""UPDATE Asset_SSID SET Change_Date=%s WHERE Ssid=%s""", (change_dt,rec1))
              cursor.close()
           db.commit()
           save_recs1=True
        for rec1 in dbssid:
           if rec1 not in tssid:
              print("checking in db data :",rec1)
              
        for rec2 in tssid:
           if rec2 not in dbssid:
              print("checking in json :",rec2)
              cursor=db.cursor() 
              cursor.execute("""INSERT INTO Asset_SSID(Ssid,Change_Date,Room_id) VALUES (%s,%s,%s)""",(rec2,change_dt,roomid))
              cursor.close()
           db.commit()
           save_recs2=True
        if(save_recs1==True or save_revs2==True):
           output = '{"error_code":"0", "Response":"Successfully added/updated the ssid status to room : %s"}' %(roomid)
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output) 
        #4th  version comments start
        '''
        for ssid1 in tssid:
           ssid1=ssid1.strip()
           ele = tssid.index(ssid1)
           print("in for")
           cursor = db.cursor()
           #new code
           print(ssid1)
           cursor.execute("SELECT Room_id FROM Asset_SSID WHERE Ssid=%s",[ssid1])
           ck_room_recs = cursor.fetchone()
           cursor.close()
           print(ck_room_recs)           
           for rec in ck_room_recs:
              rooms=str(rec)
              print("inside 2 for",rooms)
              if(rooms==str(roomid)):
                 print("same",rec)
              else:
                 print("not same")
                 cursor = db.cursor()
                 print(roomid,ssid1)
                 cursor.execute ("""UPDATE Asset_SSID SET Room_id=%s WHERE Ssid=%s""", (roomid,ssid1))
                 #savedata=Asset_SSID.objects.filter(Ssid=ssid1).update(Room_id=roomid)
                 #savedata.save()
                 db.commit()
                 cursor.close()
                 print("not same")
           print("out in")

        print("out out")
        #get the status from DB
        for ssid1 in tssid:
           ssid1=ssid1.strip()
           ele = tssid.index(ssid1)
           print("in for")
           #

           #new code
           cursor.execute("SELECT * FROM Asset_SSID WHERE Ssid=%s",[ssid1])
           ck_room_recs = cursor.fetchall()
           print(ck_room_recs)           
           if(len(ck_room_recs) > 0 ):
              print("inside if")
              for rec in ck_room_recs:
                 rooms=str(rec[3])
                 print("inside 2 for",rooms)
                 
                 if(rooms==roomid):
            
                    print("same",rec[3])
                 else:
                    savedata=Asset_SSID.objects.filter(Ssid=ssid1).update(Room_id=roomid)
                    savedata.save()
                    print("not same")
           #new code
           #
           updt_str_recs = Asset_Ssid_Str.objects.filter(Room_id=roomid,Ssid=ssid1).update(Str_ssid=tstr[ele],Change_Date=change_dt)
           print(updt_str_recs)
           if(updt_str_recs > 0 ):
              
              save_recs1=True
              print("rec there")
           else:
              print("rec not there")
              cursor=db.cursor()
              cursor.execute("""INSERT INTO Asset_Ssid_Str(Str_ssid,Change_Date,Room_id,Ssid) VALUES (%s,%s,%s,%s)""",(tstr[ele],change_dt,roomid,ssid1))
              db.commit()
              cursor.close()
              #add_str_recs = Asset_Ssid_Str(Str_ssid=tstr[ele],Change_Date=change_dt,Room_id=roomid,Ssid=ssid1)
              #add_str_recs.save()
              #if(add_str_recs > 0 ):
              save_recs2=True
              #   print("not rec there")
           #
           else:
              print("rec not thre")
              get_str_recs = Asset_Rooms.objects.filter(Room_id=roomid)
              if(get_str_recs>0):
                 get_str_recs1 = Asset_SSID.objects.filter(Ssid=ssid1)
                 if(get_str_recs1>0):
                    updt_str_recs2 = Asset_Ssid_Str(Room_id=roomid,Ssid=ssid1,Str_ssid=tstr[ele],Change_Date=change_dt)
              else:
                 get_str_recs2 = Asset_Rooms(Room_id=roomid,Room_desc=roomid,Change_Date=change_dt)
                 if(updt_str_recs1 > 0):
                    updt_str_recs2 = Asset_Ssid_Str(Room_id=roomid,Ssid=ssid1,Str_ssid=tstr[ele],Change_Date=change_dt)  	
                    if(updt_str_recs2>0):
                  save_recs2=True 

           #
        if(save_recs1==True or save_recs2==True):
           #
           list1=[]
           list2=[]
           list3=[]
           get_rooms_ssid_rec1 = Asset_Ssid_Str.objects.filter(Room_id=roomid)
           if(len(get_rooms_ssid_rec1) > 0):
           print("inside if")
           for rec in get_rooms_ssid_rec1:
              print("inside for",rec)
              add1=rec.Str_ssid
              add2=rec.Room_id.Room_id
              add3=rec.Ssid.Ssid
              print(rec.Str_ssid)
              list1.append(add1)
              list2.append(add2)
              list3.append(add3)
           minStr=list1.index(min(list1))
           print(list1)
           print(minStr)
           print(list2)
           roomname=list2[minStr]
           ssidname=list3[minStr]
           print(roomname)
           print(ssidname)
           update_rec=Asset_SSID.objects.filter(Ssid=ssidname).update(Room_id=roomname,Change_Date=change_dt)
           if(update_rec > 0):
              print("update success") 
           #
           output = '{"error_code":"0", "Response":"Successfully added the ssid status to room : %s"}' %(roomid)
           logging.debug("add_ssid_status:"+ output)
           return HttpResponse(output) 
      #}'''
        #4th version code end 
     except Exception, e:
     #{
         err_desc = 'add_ssid_status:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_ssid_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the ssid status to room}' 
         logging.debug("add_ssid_status:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_ssid_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_rooms_ssid:"+ output)
      return HttpResponse(output)



########################################################################

