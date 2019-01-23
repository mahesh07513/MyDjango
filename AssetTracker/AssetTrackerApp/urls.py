from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from AssetTrackerApp.views import *

urlpatterns = [
    url(r'^get_rooms/', csrf_exempt(get_rooms), name='get_rooms'),
    url(r'^get_rooms_ssid/', csrf_exempt(get_rooms_ssid), name='get_rooms_ssid'),
    url(r'^add_rooms_ssid/', csrf_exempt(add_rooms_ssid), name='add_rooms_ssid'),
    url(r'^add_ssid_status/', csrf_exempt(add_ssid_status), name='add_ssid_status'),

]

