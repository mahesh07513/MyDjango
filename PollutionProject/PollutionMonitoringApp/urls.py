from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from PollutionMonitoringApp.views import *

urlpatterns = [
    url(r'^add_curr_status/', csrf_exempt(add_curr_status), name='add_curr_status'),
    url(r'^del_curr_status/', csrf_exempt(del_curr_status), name='del_curr_status'),
    url(r'^get_curr_status/', csrf_exempt(get_curr_status), name='get_curr_status'),
    url(r'^get_curr_status_history/', csrf_exempt(get_curr_status_history), name='get_curr_status_history'),
    url(r'^get_excelSheet/', csrf_exempt(get_excelSheet), name='get_excelSheet'),
    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^get_top_violators/', csrf_exempt(get_top_violators), name='get_top_violators'),
    url(r'^send_messege/', csrf_exempt(send_messege), name='send_messege'),
    url(r'^add_user/', csrf_exempt(add_user), name='add_user'),
    url(r'^get_all_ids/', csrf_exempt(get_all_ids), name='get_all_ids'),


]

