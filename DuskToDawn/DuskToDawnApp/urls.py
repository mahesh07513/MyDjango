from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from DuskToDawnApp.views import *

urlpatterns = [
    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^delete_unit/', csrf_exempt(delete_unit), name='delete_unit'),
]

