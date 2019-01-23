from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from AmbienceApp.views import *

urlpatterns = [
    #url(r'^send_request/', csrf_exempt(send_request), name='send_request'),
    url(r'^get_current_setting/', csrf_exempt(get_current_setting), name='get_current_setting'),
    url(r'^add_light_position/', csrf_exempt(add_light_position), name='add_light_position'),
    url(r'^get_org_type/', csrf_exempt(get_org_type), name='get_org_type'),
    url(r'^add_user/', csrf_exempt(add_user), name='add_user'),
    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^get_orgs/', csrf_exempt(get_orgs), name='get_orgs'),
    url(r'^add_premise/', csrf_exempt(add_premise), name='add_premise'),
    url(r'^add_space/', csrf_exempt(add_space), name='add_space'),
    url(r'^get_premise/', csrf_exempt(get_premise), name='get_premise'),
    url(r'^get_spaces/', csrf_exempt(get_spaces), name='get_spaces'),

]
