from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from JtsImagesApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import FileView
urlpatterns = [
   
     url(r'^get_jts_images/', csrf_exempt(get_jts_images), name='get_jts_images'),
     url(r'^add_image/', csrf_exempt(add_image), name='add_image'),
     url(r'^get_images/', csrf_exempt(get_images), name='get_images'),
     url(r'^upload/$', FileView.as_view(), name='file-upload'),


]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


