from rest_framework import serializers
from .models import JTS_Images
class FileSerializer(serializers.ModelSerializer):
  #Image=serializers.ImageField(max_length=None,use_url=True)
  class Meta():
    model = JTS_Images
    fields = ('ImgId', 'Image', 'ChangeDate')
