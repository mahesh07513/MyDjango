from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from UrbanKisanApp.views import *

urlpatterns = [
    url(r'^get_data/', csrf_exempt(get_data), name='get_data'),
    url(r'^get_history/', csrf_exempt(get_history), name='get_history'),
    url(r'^get_data_UB/', csrf_exempt(get_data_UB), name='get_data_UB'),
    url(r'^get_history_UB/', csrf_exempt(get_history_UB), name='get_history_UB'),

]

