from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from PowerApp.views import *

urlpatterns = [
    url(r'^get_sumary/', csrf_exempt(get_sumary), name='get_sumary'),
    url(r'^add_power_voltage/', csrf_exempt(add_power_voltage), name='add_power_voltage'),
    
    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^get_last_voltage/', csrf_exempt(get_last_voltage), name='get_last_voltage'),
    url(r'^get_modules/', csrf_exempt(get_modules), name='get_modules'),

]

