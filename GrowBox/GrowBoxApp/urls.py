from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from GrowBoxApp.views import *
from django.conf import settings
from django.conf.urls.static import static
#from .views import FileView

urlpatterns = [

#    url(r'^get_temp_history/', csrf_exempt(get_temp_history), name='get_temp_history'),
    url(r'^get_growbox_data/', csrf_exempt(get_growbox_data), name='get_growbox_data'),
    url(r'^get_ble_data/', csrf_exempt(get_ble_data), name='get_ble_data'),


]
