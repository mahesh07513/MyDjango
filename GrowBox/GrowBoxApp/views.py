from __future__ import unicode_literals
from django.shortcuts import render
#from datetime import tzinfo,timedelta
import requests
# Create your views here.
from GrowBoxApp.models import *
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
from datetime import timedelta
from django.utils import timezone
from dateutil import rrule
import itertools

# Create your views here.

#################################get temp history ####################
def get_growbox_data(request):
    #stdt="2018-09-20 00:00"
    #enddt="2018-09-25 23:59"
    #start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    #end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    #data1 = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
    one_hour_later = this_hour + timedelta(hours=1)
    data1 = GB_GrowData_History.objects.filter(ChangeDate__range=(this_hour, one_hour_later)).order_by('-ChangeDate')
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d %H:%M"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped]
    extra_context = {"data": data1}
    #print extra_context
    return render(request,"get_growbox_data.html", extra_context)
#################################get temp history ####################
def get_ble_data(request):
    #stdt="2018-09-20 00:00"
    #enddt="2018-09-25 23:59"
    #start_date = datetime.strptime(stdt, '%Y-%m-%d %H:%M')
    #end_date = datetime.strptime(enddt, '%Y-%m-%d %H:%M')
    #data1 = AC_Unit_History.objects.filter(ChangeDate__range=[start_date, end_date]).order_by('-UHId')[:200][::-1]
    this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
    one_hour_later = this_hour + timedelta(hours=2)
    data1 = BLE_Data_History.objects.filter(ChangeDate__range=(this_hour, one_hour_later)).order_by('-ChangeDate')
    #grouped = itertools.groupby(data1, lambda record: record.ChangeDate.strftime("%Y-%m-%d %H:%M"))
    #jobs_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped]
    extra_context = {"data": data1}
    #print extra_context
    return render(request,"get_ble_data.html", extra_context)


