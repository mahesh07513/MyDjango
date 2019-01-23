#from django.shortcuts import render
# Create your views here.
#from JtsImagesApp.models import Product
from __future__ import unicode_literals
from django.shortcuts import render
#from datetime import tzinfo,timedelta
import requests
# Create your views here.
from JtsImagesApp.models import *
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
import string
import random
from dateutil import rrule
import itertools
import sys
import base64
import ast
# Create your views here.
'''
def index(request):
    return render(request, 'index.html', {
        'products': Product.objects.all(),
    })

'''
###########################################################
def get_jts_images(request):
    #data1 = Oyo_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    data1 = JTS_Images.objects.filter()
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped] #
    #last_14_days = datetime.today() - datetime.timedelta(14)
    #jobs = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).values("ChangeDate")
    #grouped = itertools.groupby(jobs, lambda record: record.get("ChangeDate").strftime("%Y-%m-%d"))
    #jobs_by_day = [(hour, len(list(jobs_this_day))) for hour, jobs_this_day in grouped]

    extra_context = {"data": data1}
    #print extra_context
    return render(request,"index.html", extra_context)

##################AddImage###############################
def add_image(request):  

   if(request.method == "POST"):
   #{
     logging.debug("add_image: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "add_image- Unable to Authenticate/add_image... "
     try:
        data1 = json.loads(request.body)
        #print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
        logging.debug("add_image:"+ output)
        HttpResponse(output)

     try:

     #{
        if(not data1):
          output_str += ", details are mandatory"
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str)
          logging.debug("add_image:"+ output)
          return HttpResponse(output)

        if(data1.get('username') is None):
          output_str += ",username is mandatory"
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_image:"+ output)
          return HttpResponse(output)

        if(data1.get('password') is None):
          output_str += ",passsword is mandatory"
          output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
          logging.debug("add_image:"+ output)
          return HttpResponse(output)

        username    = data1['username']
        password    = data1['password']
        logging.debug("add_image:input: user="+username)
        #check authentication (temporary, this will need to be implemented) 
        if(username != "admin") or (password != "admin"):
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("login:Failed to Authenticate"+ output)
           return HttpResponse(output)
        
	'''
        if((data1.get('name') is None) or ((data1.get('name') is not  None) and (len(data1['name']) <= 0))):
           output_str += ",name is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
           logging.debug("add_image:"+ output)
           return HttpResponse(output)
        else:
           name = data1['name']
        '''
        #name=id_generator() 
        name=random.randint(1,1000)
        #print name
        if((data1.get('image') is None)):
            output_str += ",image is mandatory"
            output = '{"error_code":"2", "error_desc": "%s"}' %output_str
            logging.debug("image:"+ output)
            return HttpResponse(output)

        else:
           image = data1['image']
        image_64_decode = base64.decodestring(image)
        image_result = open('/var/www/html/JtsImages/%s.jpg' %(name),'wb')
        image_result.write(image_64_decode)
        '''
        image_64_decode = base64.decodestring(image)
        image_result = open('/var/www/html/JtsImages/%s.jpg' %(name),'wb')
        image_result.write(image_64_decode)
        '''
        name1=str(name)+'.jpg'
        name2='http://cld003.jts-prod.in/JtsImages/%s' %(name1)
        #print "dataaaaa : ",name2
        #get the status from DB
        add_img_rec=JTS_Images(Image=name2,StatusActive=True);
        add_img_rec.save()
        #print "data"
        if(add_img_rec > 0):
           output = '{"error_code":"0", "Response":"Successfully added the Image"}' 
           logging.debug("add_image:"+ output)
           return HttpResponse(output)
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to add the user"}'
           logging.debug("add_image:"+ output)
           return HttpResponse(output)
  
           
     #}
     except Exception, e:
     #{
         err_desc = 'add_image:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("add_image:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to add the image"}'
         logging.debug("add_image:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("add_image: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}'
      logging.debug("add_image:"+ output)
      return HttpResponse(output)
####################get images#################
def get_images(request):

   if(request.method == "POST"):
   #{
     logging.debug("get_images: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
     output_str = "get_images - Unable to Authenticate/get_images... " 
     try:
        data1 = json.loads(request.body)
        #print request.body
     except ValueError:
        output_str += ",invalid input, no proper JSON request "
        output = '{"error_code":"2", "error_desc": "Response=%s"}' %(output_str )
        logging.debug("get_images:"+ output)
        return HttpResponse(output)
     try:
     #{
          
        if(data1.get('username') is None):
           output_str += ",username is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_images:"+ output)
           return HttpResponse(output)

        if(data1.get('password') is None):
           output_str += ",passsword is mandatory"
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("get_images:"+ output)
           return HttpResponse(output)

        username    = data1['username']
        password    = data1['password']
        logging.debug("get_images:input: user="+username)
        if(username != "admin") or (password != "admin"):
           output = '{"error_code":"2", "error_desc": "Response=%s"}' %output_str
           logging.debug("login:Failed to Authenticate"+ output)
           return HttpResponse(output)
         
        kwargs = {}

       
        #Get the Curent_Status records
        get_images_rec = JTS_Images.objects.filter(**kwargs)
        if(len(get_images_rec) > 0): 
        #{
           output = '{"error_code":"0", "Response":"Successfully got %d images", \n "get_images":' %len(get_images_rec)
           output += '['
           counter = 0
           for rec in get_images_rec:
           #{
              counter += 1
              if(counter == 1):
                output += '{"image_id":"%s","image_desc":"%s"}' %(rec.ImgId ,rec.Image)
              else: 
                output += ',\n {"image_id":"%s","image_desc":"%s"}' %(rec.ImgId ,rec.Image)
           #}
           output += ']\n'
           output += '}'
           #cust_recs_json = serializers.serialize("json", curr_status_recs)
           logging.debug("get_images:"+ output)
           return HttpResponse(output)
        #}
        else:
           output = '{"error_code":"3", "error_desc": "Response=Failed to get the image records, NO_DATA_FOUND"}' 
           logging.debug("get_images:"+ output)
           return HttpResponse(output)
     #}
     except Exception, e:
     #{
         err_desc = 'get_images:exception details:[%s],[%s]' %((sys.exc_info()[0]), (sys.exc_info()[1]))
         logging.debug("get_images:"+ err_desc)
         output = '{"error_code":"3", "error_desc": "Response=Failed to get the image"}' 
         logging.debug("get_images:"+ output)
         return HttpResponse(output)
     #}
   #}
   else:
      logging.debug("get_images: request is from the IP:%s" %request.META.get('REMOTE_ADDR'))
      output = '{"error_code":"3", "error_desc": "Response=GET is not supported"}' 
      logging.debug("get_images:"+ output)
      return HttpResponse(output)

####################################################
def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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


