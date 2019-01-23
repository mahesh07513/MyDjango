from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from FMSApp.views import *

urlpatterns = [
    #url(r'^paypal/', csrf_exempt(paypal), name='paypal'),
]
