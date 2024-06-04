from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class SimpleProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
  following = SimpleProfileSerializer(many=True, read_only =True)
  followers = SimpleProfileSerializer(many=True, read_only =True)

  class Meta:
    model = Profile
    fields = '__all__'


# class ImageSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Image
#     fields = ['id', 'title', 'image', 'created_at']