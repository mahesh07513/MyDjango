from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from GenericACApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import FileView
#from django.urls import include, path
#from . import views

urlpatterns = [
#    url(r'^add_user/', csrf_exempt(add_user), name='add_user'),
#    url(r'^login/', csrf_exempt(login), name='login'),
#    url(r'^get_roles/', csrf_exempt(get_roles), name='get_roles'),
#    url(r'^get_premise/', csrf_exempt(get_premise), name='get_premise'),
#    url(r'^get_units/', csrf_exempt(get_units), name='get_units'),
#    url(r'^get_floors/', csrf_exempt(get_floors), name='get_floors'),
#    url(r'^get_rooms/', csrf_exempt(get_rooms), name='get_rooms'),
#    url(r'^get_units_details/', csrf_exempt(get_units_details), name='get_units_details'),
    url(r'^delete_premise/', csrf_exempt(delete_premise), name='delete_premise'),
    url(r'^delete_city/', csrf_exempt(delete_city), name='delete_city'),
    url(r'^delete_floor/', csrf_exempt(delete_floor), name='delete_floor'),
    url(r'^delete_room/', csrf_exempt(delete_room), name='delete_room'),
    url(r'^delete_unit/', csrf_exempt(delete_unit), name='delete_unit'),
    url(r'^delete_unit_utype/', csrf_exempt(delete_unit_utype), name='delete_unit_utype'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),

#    url(r'^get_temp_history/', csrf_exempt(get_temp_history), name='get_temp_history'),
    url(r'^get_power_data/', csrf_exempt(get_power_data), name='get_power_data'),
    url(r'^get_drop_down/', csrf_exempt(get_drop_down), name='get_drop_down'),
    url(r'^get_data/', csrf_exempt(get_data), name='get_data'),
    #path('get_data/', views.get_data, name='get_data'),

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

