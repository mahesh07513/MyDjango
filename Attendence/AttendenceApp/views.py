from __future__ import unicode_literals

from django.shortcuts import render
from geopy.geocoders import GoogleV3
# Create your views here.

from AttendenceApp.models import *
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
#db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
# Create your views here.
##########################################################
def add_employee(request):  #this will add/update the status
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("add_employee: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_employee - Unable to Authenticate/add_employee... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_employee:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", All details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_employee:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
	#username
        if((data1.get('name') is None) or ((data1.get('name') is not  None) and (len(data1['name']) <= 0))):
           output_str += ", name is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           name = data1['name']   
           #print("this is pass:"+login)
        '''
        #password
        if((data1.get('password') is None) or ((data1.get('password') is not  None) and (len(data1['password']) <= 0))):
           output_str += ",password is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           password = data1['password']
           #print("this is loginType",logintype) 
        '''
        #mobile
   
        if((data1.get('mobile') is None) or ((data1.get('mobile') is not  None) and (len(data1['mobile']) <= 0))):
           output_str += ", mobile is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           mobile = data1['mobile']
           #print("this is pass:"+username)   
           

        #email
        if((data1.get('email') is None) or ((data1.get('email') is not  None) and (len(data1['email']) <= 0))):
           output_str += ",email is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           email = data1['email']
           #print("this is pass:"+phone)
  	  
        #role
        if((data1.get('role') is None) or ((data1.get('role') is not  None) and (len(data1['role']) <= 0))):
           output_str += ", role is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           role = data1['role']
           #print("this is pass:"+emailid)   

        #specs
        if((data1.get('specs') is None) or ((data1.get('specs') is not  None) and (len(data1['specs']) <= 0))):
           output_str += ", specs is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        else:
           role = data1['specs']
        '''
        #get the rec from DB
        is_rec_needed = False
        if Light_Users.objects.filter(Username = username,Password=password).exists():
               
           is_rec_needed = True
           #print("matching")
        else:
           is_rec_needed = False
           output = '{"error_code":"4", "error_desc": "Response= You have No right to Add/Modify."}'
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        '''   
        #check authentication (temporary, this will need to be implemented) 
        if(username != "admin") or (password != "admin"):
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("login:Failed to Authenticate"+ output)
           return HttpResponse(output)        
        else:
           is_rec_needed = True           


        if is_rec_needed==True: 
          print("inside the true1")
          add_emply_rec = Employee_Details(name=name,mobile=mobile,email=email,role=role,spec=spec)
          add_emply_rec.save()
          print("inside the true2")
          if(len(str(add_emply_rec.ChangeDate)) > 0 ): #If there is an exception, it will not come here
            output = '{"error_code":"0", "Response":"Successfully added the employee :%s"}' %(name)
            logging.debug("add_employee:"+ output)
            return HttpResponse(output)
                         
     #}
     
     except Exception, e:
     #{
         err_desc = 'add_employee:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_employee:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add premisis"}' 
         logging.debug("add_employee:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_employee: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_employee:"+ output)
      return HttpResponse(output)

#####################################################################################
def get_status(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_status- Unable to Authenticate/get_status... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_status:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_status:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_status:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_status:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_status:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_employee:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
       

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        ''' 
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("SELECT id,statusName FROM inv_status WHERE id>=19 and id<=22")
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d status", \n "get_status":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"sid":"%s","sname":"%s"}' %(rec[0],rec[1])
              else: 
                 output += ',\n {"sid":"%s","sname":"%s"}' %(rec[0],rec[1])
          
           output += ']\n'
           output += '}'
           logging.debug("get_status:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the status records, NO_DATA_FOUND"}' 
           logging.debug("get_status:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_employee:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the status"}' 
         logging.debug("get_status:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_status:"+ output)
      return HttpResponse(output)

###################################################################################
def get_sales_category(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_sales_category: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_sales_category- Unable to Authenticate/get_sales_category... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_sales_category:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_sales_category:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_sales_category:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_sales_category:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_sales_category:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_sales_category:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
       

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        ''' 
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("SELECT * FROM sales_category")
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d sales_category", \n "get_sales_category":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"scid":"%s","scname":"%s"}' %(rec[0],rec[1])
              else: 
                 output += ',\n {"scid":"%s","scname":"%s"}' %(rec[0],rec[1])
          
           output += ']\n'
           output += '}'
           logging.debug("get_sales_category:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the sales_category records, NO_DATA_FOUND"}' 
           logging.debug("get_sales_category:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_sales_category:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_sales_category:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the sales_category"}' 
         logging.debug("get_sales_category:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_sales_category: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_sales_category:"+ output)
      return HttpResponse(output)
#
####################################################################################
def get_employee(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_employee: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_employee- Unable to Authenticate/get_employee... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_employee:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_employee:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_employee:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_employee:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_employee:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_employee:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("SELECT id,userName FROM jts_employees")
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d employees", \n "get_employee":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"eid":"%s","ename":"%s"}' %(rec[0],rec[1])
              else: 
                 output += ',\n {"eid":"%s","ename":"%s"}' %(rec[0],rec[1])
          
           output += ']\n'
           output += '}'
           logging.debug("get_employee:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the employee records, NO_DATA_FOUND"}' 
           logging.debug("get_employee:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_employee:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_employee:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the employees"}' 
         logging.debug("get_employee:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_employee: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_employee:"+ output)
      return HttpResponse(output)
##############################################################################################################

def get_role(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_role: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_role- Unable to Authenticate/get_role... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_role:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_role:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_role:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_employee:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_role:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_role:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
        '''

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("SELECT jobRole FROM emp_jobrole")
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d employees", \n "get_employee":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"role":"%s"}' %(rec[0])
              else: 
                 output += ',\n {"role":"%s"}' %(rec[0])
          
           output += ']\n'
           output += '}'
           logging.debug("get_role:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the employee records, NO_DATA_FOUND"}' 
           logging.debug("get_role::"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_role::exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_role::"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the employees"}' 
         logging.debug("get_role::"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_role:: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_role::"+ output)
      return HttpResponse(output)

#####################################################################################################
def get_customer(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_customer: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_customer- Unable to Authenticate/get_customer... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_customer:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_customer:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_customer:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
        

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        '''        
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("SELECT customerName,Contact,Address,dateOfVisit,salesCategory FROM inv_forecast")
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d employees", \n "get_employee":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"cname":"%s","contact":"%s","address":"%s","visitdate":"%s","category":"%s"}' %(rec[0],rec[1],rec[2],rec[3],rec[4])
              else: 
                 output += ',\n {"cname":"%s","contact":"%s","address":"%s","visitdate":"%s","category":"%s"}' %(rec[0],rec[1],rec[2],rec[3],rec[4])
          
           output += ']\n'
           output += '}'
           logging.debug("get_customer:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the customer records, NO_DATA_FOUND"}' 
           logging.debug("get_customer:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_role::exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_customer:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the customers"}' 
         logging.debug("get_customer:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_customer: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_customer:"+ output)
      return HttpResponse(output)

#############################################################################################
def get_customer_map(request):
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_customer_map: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_customer_map- Unable to Authenticate/get_customer_map... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_customer_map:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_customer_map:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer_map:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer_map:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_customer_map:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_customer_map:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:
     #{
        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
        

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        '''   
        if((data1.get('lat') is None) or ((data1.get('lat') is not  None) and (len(data1['lat']) <= 0))):
           output_str += ", lat is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee_map:"+ output)
           return HttpResponse(output)
        else:
           lat = data1['lat'] 
           lat = lat[:-5] 
        
	if((data1.get('lag') is None) or ((data1.get('lag') is not  None) and (len(data1['lag']) <= 0))):
           output_str += ", lag is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_employee_map:"+ output)
           return HttpResponse(output)
        else:
           lag = data1['lag']
           lag = lag[:-5]
        '''
        #lan = round(float(lan), 3)
        #lag = round(float(lag), 3)
	lat1=float(lat)
        print(lat1)
        print("%.2f" % 1.923328437452)
        lat1="%.2f" % lat1
        print(lat1)
        lag1=float(lag)
        print(lag1)
        lag1="%.2f" % lag1
        print(lag1)       
        
       
        geocoder = GoogleV3()
        location_list = geocoder.reverse((lan, lag))
        print(location_list)
        location = location_list[0]
        print(location)
        address = location.address
        print(address) 
        '''
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        longi=str(lag)+"%"
        lati=str(lat)+"%"
        #print(data)
        #print("SELECT customerName FROM inv_forecast where langitude like %s",[data])
        cursor.execute("SELECT customerName FROM inv_forecast where langitude like %s AND latitude like %s",[longi,lati])
        get_emply_recs=cursor.fetchall()
        cursor.close()
        print(get_emply_recs)
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d Clients", \n "get_clients":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              counter += 1
              if(counter == 1):
                 output += '{"cname":"%s"}' %(rec[0])
              else: 
                 output += ',\n {"cname":"%s"}' %(rec[0])
          
           output += ']\n'
           output += '}'
           logging.debug("get_customer_map:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the customer records, NO_DATA_FOUND"}' 
           logging.debug("get_customer_map:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_role::exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_customer_map:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the customers"}' 
         logging.debug("get_customer_map:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_customer_map: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_customer_map:"+ output)
      return HttpResponse(output)


############################################################################
def add_customer(request):  #this will add/update the status
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("add_customer: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_customer - Unable to Authenticate/add_customer... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_customer:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", All details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_customer:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
	#cname
        if((data1.get('cname') is None) or ((data1.get('cname') is not  None) and (len(data1['cname']) <= 0))):
           output_str += ",cname is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           cname = data1['cname']   
           print("this is cname:"+cname)
        
        
        #mobile
        if((data1.get('mobile') is None) or ((data1.get('mobile') is not  None) and (len(data1['mobile']) <= 0))):
           output_str += ", mobile is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           mobile = data1['mobile']
           print("this is mobile:"+mobile)   
           

        #email
        if((data1.get('email') is None) or ((data1.get('email') is not  None) and (len(data1['email']) <= 0))):
           output_str += ",email is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           email = data1['email']
           print("this is pass:"+email)
  	  
        #role
        if((data1.get('dueDate') is None) or ((data1.get('dueDate') is not  None) and (len(data1['dueDate']) <= 0))):
           output_str += ", dueDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           duedate = data1['dueDate']
           print("this is duedate:"+duedate)   
         
        if((data1.get('dateOfVisit') is None) or ((data1.get('dateOfVisit') is not  None) and (len(data1['dateOfVisit']) <= 0))):
           output_str += ", dateOfVisit is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           dateOfVisit = data1['dateOfVisit']
           print("this is visit:"+dateOfVisit)
 
        #specs
        if((data1.get('address') is None) or ((data1.get('address') is not  None) and (len(data1['address']) <= 0))):
           output_str += ", address is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           address = data1['address']
           print("this is address:"+address)

        if((data1.get('statusId') is None) or ((data1.get('statusId') is not  None) and (len(data1['statusId']) <= 0))):
           output_str += ", statusId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           statusId = data1['statusId']
           print("this is statusid:"+statusId)
        if((data1.get('userId') is None) or ((data1.get('userId') is not  None) and (len(data1['userId']) <= 0))):
           output_str += ", userId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           userId = data1['userId']  
           print("this is userId:"+userId)
        if((data1.get('salesCategory') is None) or ((data1.get('salesCategory') is not  None) and (len(data1['salesCategory']) <= 0))):
           output_str += ", salesCategory is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           salesCategory = data1['salesCategory']
           print("this is sales:"+salesCategory)

        if((data1.get('langitude') is None) or ((data1.get('langitude') is not  None) and (len(data1['langitude']) <= 0))):
           output_str += ", langitude is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           langitude = data1['langitude']
           print("this is lan:"+langitude)

        if((data1.get('latitude') is None) or ((data1.get('latitude') is not  None) and (len(data1['latitude']) <= 0))):
           output_str += ", latitude is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_customer:"+ output)
           return HttpResponse(output)
        else:
           latitude = data1['latitude']
           print("this is lat:"+latitude)
        is_rec_check = True
        username=data1['username']
        password=data1['password']
        is_rec_needed = False
        '''
        #get the rec from DB
        is_rec_needed = False
        if Light_Users.objects.filter(Username = username,Password=password).exists():
               
           is_rec_needed = True
           #print("matching")
        else:
           is_rec_needed = False
           output = '{"error_code":"4", "error_desc": "Response= You have No right to Add/Modify."}'
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        '''   
        #check authentication (temporary, this will need to be implemented) 
        if(username != "admin") or (password != "admin"):
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("login:Failed to Authenticate"+ output)
           return HttpResponse(output)        
        else:
           is_rec_needed = True 
           print("auth ok")
           
           cursor=db.cursor()
           check_row = cursor.execute("SELECT customerName FROM inv_forecast WHERE customerName=%s",[cname])
           cursor.fetchone()
           if check_row > 0:
              is_rec_check=True
              output = '{"error_code":"4", "error_desc": "Response=customer name already exists}'
              logging.debug("add_customer:customer name already exists"+ output)
              return HttpResponse(output)
           else:
              is_rec_check=False
           
        print("came",dateOfVisit)          
        dateOfVisit1 = datetime.strptime(dateOfVisit, '%Y-%m-%d')
        print(dateOfVisit1)
        duedate1 = datetime.strptime(duedate, '%Y-%m-%d')
        print("came2",duedate1)
        if is_rec_needed==True: 
          print("inside the true1")
          cursor=db.cursor()
          print("INSERT INTO inv_forecast(customerName,Contact,emailId,Address,dateOfVisit,statusId,userId,salesCategory,langitude,latitude) VALUES (%s,%s,%s,%s,%s,%d,%d,%d,%s,%s)",(cname,mobile,email,address,dateOfVisit1,int(statusId),int(userId),int(salesCategory),langitude,latitude))
         
          add_cus_rec = cursor.execute("""INSERT INTO inv_forecast(customerName,Contact,emailId,Address,dateOfVisit,dueDate,statusId,userId,salesCategory,langitude,latitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(cname,mobile,email,address,dateOfVisit1,duedate1,int(statusId),int(userId),int(salesCategory),langitude,latitude))
          #add_emply_rec = inv_forecast(customerName=cname,Contact=mobile,emailId=email,Address=address,dueDate=duedate,dateOfVisit=dateOfVisit,statusId=statusId,userId=userId,salesCategory=salesCategory,langitude=langitude,latitude=latitude)
          #add_emply_rec.save()
          print("came 3")
          cursor.close()
          db.commit()
          cursor=db.cursor()
          
          add_cus_rec1 = cursor.execute("""INSERT INTO jts_cus_logs(cusId,userId,ChangeDate,statusId) VALUES (%s,%s,%s,%s)""",(cname,int(userId),dateOfVisit1,int(statusId)))
          #add_emply_rec = inv_forecast(customerName=cname,Contact=mobile,emailId=email,Address=address,dueDate=duedate,dateOfVisit=dateOfVisit,statusId=statusId,userId=userId,salesCategory=salesCategory,langitude=langitude,latitude=latitude)
          #add_emply_rec.save()
          print("came 3")
          cursor.close()
          db.commit()


 
          print("inside the true2")
          if(add_cus_rec > 0 and add_cus_rec1 > 0): #If there is an exception, it will not come here
            output = '{"error_code":"0", "Response":"Successfully added the customer :%s"}' %(cname)
            logging.debug("add_customer:"+ output)
            return HttpResponse(output)
                         
     #}
     
     except Exception, e:
     #{
         err_desc = 'add_customer:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_customer:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add_customer"}' 
         logging.debug("add_customer:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_customer: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_customer:"+ output)
      return HttpResponse(output)
################################################################################################
def add_cus_logs(request):  #this will add/update the status
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("add_customer: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_cus_logs - Unable to Authenticate/add_cus_logs... " 
     try:
        data1 = json.loads(request.body)
	print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_cus_logs:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", All details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("add_cus_logs:"+ output)
        return HttpResponse(output)

       
   
     try:
     #{
	#cname
        if((data1.get('cname') is None) or ((data1.get('cname') is not  None) and (len(data1['cname']) <= 0))):
           output_str += ",cname is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           cname = data1['cname']   
           print("this is cname:"+cname)
        
        
        if((data1.get('dateOfVisit') is None) or ((data1.get('dateOfVisit') is not  None) and (len(data1['dateOfVisit']) <= 0))):
           output_str += ", dateOfVisit is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           dateOfVisit = data1['dateOfVisit']
           print("this is visit:"+dateOfVisit)
 
        if((data1.get('statusId') is None) or ((data1.get('statusId') is not  None) and (len(data1['statusId']) <= 0))):
           output_str += ", statusId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           statusId = data1['statusId']
           print("this is statusid:"+statusId)
        
        if((data1.get('userId') is None) or ((data1.get('userId') is not  None) and (len(data1['userId']) <= 0))):
           output_str += ", userId is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           userId = data1['userId']  
           print("this is userId:"+userId)
        if((data1.get('notes') is None) or ((data1.get('notes') is not  None) and (len(data1['notes']) <= 0))):
           output_str += ", notes is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           notes = data1['notes']
           print("this is userId:"+notes)
   
        if((data1.get('nextdate') is None) or ((data1.get('nextdate') is not  None) and (len(data1['nextdate']) <= 0))):
           output_str += ", nextdate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           nextdate = data1['nextdate']
           print("this is userId:"+nextdate)        

        username=data1['username']
        password=data1['password']
        is_rec_needed = False  
        '''
        #get the rec from DB
        if Light_Users.objects.filter(Username = username,Password=password).exists():
               
           is_rec_needed = True
           #print("matching")
        else:
           is_rec_needed = False
           output = '{"error_code":"4", "error_desc": "Response= You have No right to Add/Modify."}'
           logging.debug("add_employee:"+ output)
           return HttpResponse(output)
        '''   
        #check authentication (temporary, this will need to be implemented) 
        if(username != "admin") or (password != "admin"):
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("login:Failed to Authenticate"+ output)
           return HttpResponse(output)        
        else:
           #is_rec_needed = True 
           print("auth ok")
           
           cursor=db.cursor()
           check_row = cursor.execute("SELECT customerName FROM inv_forecast WHERE customerName=%s",[cname])
           cursor.fetchone()
           if check_row > 0:
              is_rec_needed = True 
           
        print("came",dateOfVisit)          
        dateOfVisit1 = datetime.strptime(dateOfVisit, '%Y-%m-%d')
        print(dateOfVisit1)
        nextdate1 = datetime.strptime(nextdate, '%Y-%m-%d')
        print(nextdate1)
        if is_rec_needed==True: 
          print("inside the true1")
          cursor=db.cursor()
          print("INSERT INTO jts_cus_logs(cusId,ChangeDate,statusId,userId) VALUES (%s,%s,%d,%d)",(cname,dateOfVisit1,int(statusId),int(userId)))
         
          add_cus_rec = cursor.execute("""INSERT INTO jts_cus_logs(cusId,ChangeDate,statusId,userId,notes,notesDate) VALUES (%s,%s,%s,%s,%s,%s)""",(cname,dateOfVisit1,int(statusId),int(userId),notes,nextdate1))
          #add_emply_rec = inv_forecast(customerName=cname,Contact=mobile,emailId=email,Address=address,dueDate=duedate,dateOfVisit=dateOfVisit,statusId=statusId,userId=userId,salesCategory=salesCategory,langitude=langitude,latitude=latitude)
          #add_emply_rec.save()
          print("came 3")
          cursor.close()
          db.commit()
          cursor=db.cursor()
                 
          print("inside the true2")
          if(add_cus_rec > 0 ): #If there is an exception, it will not come here
            output = '{"error_code":"0", "Response":"Successfully added the customer report :%s"}' %(cname)
            logging.debug("add_cus_logs:"+ output)
            return HttpResponse(output)
                         
     #}
     
     except Exception, e:
     #{
         err_desc = 'add_cus_logs:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_cus_logs:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add_cus_logsr"}' 
         logging.debug("add_cus_logs:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_cus_logs: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("add_cus_logs:"+ output)
      return HttpResponse(output)

###################################################################################################
def get_cus_logs(request):
   
   db = MySQLdb.connect("localhost","inventory","jtsinv","inventoryapp")
   if(request.method == "POST"):
   #{
     logging.debug("get_cus_logs: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_cus_logs- Unable to Authenticate/get_cus_logs... " 
     try:
        data1 = json.loads(request.body)
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_cus_logs:"+ output)
        return HttpResponse(output)
     
     if(not data1):
        output_str += ", Details are mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_cus_logs:"+ output)
        return HttpResponse(output)

     if(data1.get('username') is None):
        output_str += ",username is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_cus_logs:"+ output)
        return HttpResponse(output)

     if(data1.get('password') is None):
        output_str += ",passsword is mandatory"
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_cus_logs:"+ output)
        return HttpResponse(output)

     username    = data1['username']
     password    = data1['password']
     logging.debug("get_cus_logs:input: user="+username)
     
     #check authentication (temporary, this will need to be implemented) 
     if(username != "admin") or (password != "admin"):
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
        logging.debug("get_cus_logs:Failed to Authenticate"+ output)
        return HttpResponse(output)
       
     
     check_login_authenticate=False
     try:

        if((data1.get('fromDate') is None) or ((data1.get('fromDate') is not  None) and (len(data1['fromDate']) <= 0))):
           output_str += ", fromDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           fromDate = data1['fromDate']
           print("this is fromDate:"+fromDate)

        if((data1.get('toDate') is None) or ((data1.get('toDate') is not  None) and (len(data1['toDate']) <= 0))):
           output_str += ", toDate is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_cus_logs:"+ output)
           return HttpResponse(output)
        else:
           toDate = data1['toDate']
           print("this is toDate:"+toDate)

        '''
        if Light_Users.objects.filter(Username = username,Password=password).exists():
           print("data success")
        else:
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("get_premisis:Failed to Authenticate"+ output)
          return HttpResponse(output)
       

        kwargs = {}
        ename=""
        check_premisis=False
        if((data1.get('name') is not  None) and (len(data1['name']) > 0)):
           ename = data1['name']   
           kwargs['name'] = ename        
           #check_premisis=True
        ''' 
        fromDate1 = datetime.strptime(fromDate, '%Y-%m-%d')
        toDate1 = datetime.strptime(toDate, '%Y-%m-%d')
        print("date")
        #get emplyee data
        #get_emply_recs = Light_Premisis.objects.filter(**kwargs)
        cursor=db.cursor()
        cursor.execute("select cusId,jts_employees.userName,inv_status.statusName,ChangeDate from inv_status,jts_employees,jts_cus_logs where jts_cus_logs.userId=jts_employees.id and jts_cus_logs.statusId=inv_status.id and ChangeDate>=%s and ChangeDate<=%s ",[fromDate1,toDate1])
        get_emply_recs=cursor.fetchall()
        cursor.close()
        if(len(get_emply_recs) > 0): 
           print("in")
           output = '{"error_code":"0", "Response":"Successfully got %d status", \n "get_cus_logs":' %len(get_emply_recs)
           output += '['
           counter = 0
           for rec in get_emply_recs:
              #visitdate = datetime.strptime(rec[3], '%Y-%m-%d')
              counter += 1
              if(counter == 1):
                 output += '{"cname":"%s","ename":"%s","status":"%s","visitDate":"%s"}' %(rec[0],rec[1],rec[2],rec[3])
              else: 
                 output += ',\n {"cname":"%s","ename":"%s","status":"%s","visitDate":"%s"}' %(rec[0],rec[1],rec[2],rec[3])
          
           output += ']\n'
           output += '}'
           logging.debug("get_cus_logs:"+ output)
           return HttpResponse(output)
        
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the status records, NO_DATA_FOUND"}' 
           logging.debug("get_cus_logs:"+ output)
           return HttpResponse(output)
                  

     except Exception, e:
     
         err_desc = 'get_cus_logs:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_status:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the cus_logs"}' 
         logging.debug("get_cus_logs:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_status: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_cus_logs:"+ output)
      return HttpResponse(output)




