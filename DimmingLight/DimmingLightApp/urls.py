from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from DimmingLightApp.views import *

urlpatterns = [
    url(r'^add_modes/', csrf_exempt(add_modes), name='add_modes'),
    url(r'^get_modes/', csrf_exempt(get_modes), name='get_modes'),    
    url(r'^get_mode_settings/', csrf_exempt(get_mode_settings), name='get_mode_settings'),

]


