from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from PrepaidRCApp.views import *

urlpatterns = [
    url(r'^add_charge/', csrf_exempt(add_charge), name='add_charge'),
]

