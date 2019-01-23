from rest_framework import serializers
from .models import AC_Images
class FileSerializer(serializers.ModelSerializer):
  #Image=serializers.ImageField(max_length=None,use_url=True)
  class Meta():
    model = AC_Images
    fields = ('ImgId', 'Image', 'ChangeDate')
