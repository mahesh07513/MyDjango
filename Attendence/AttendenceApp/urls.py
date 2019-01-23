from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from AttendenceApp.views import *

urlpatterns = [
    url(r'^add_employee/', csrf_exempt(add_employee), name='add_employee'),
    url(r'^get_employee/', csrf_exempt(get_employee), name='get_employee'),
    url(r'^get_role/', csrf_exempt(get_role), name='get_role'),    
    url(r'^get_customer/', csrf_exempt(get_customer), name='get_customer'),
    url(r'^get_customer_map/', csrf_exempt(get_customer_map), name='get_customer_map'),
    url(r'^get_sales_category/', csrf_exempt(get_sales_category), name='get_sales_category'),
    url(r'^get_status/', csrf_exempt(get_status), name='get_status'),
    url(r'^add_customer/', csrf_exempt(add_customer), name='add_customer'),
    url(r'^add_cus_logs/', csrf_exempt(add_cus_logs), name='add_cus_logs'),
    url(r'^get_cus_logs/', csrf_exempt(get_cus_logs), name='get_cus_logs'),


]

