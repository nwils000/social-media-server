from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class SimpleProfileSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Profile
    fields = ['user', 'id', 'first_name', 'last_name']

class LikeSerializer(serializers.ModelSerializer):
    profile = SimpleProfileSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'profile', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    profile = SimpleProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
  

class PostSerializer(serializers.ModelSerializer):
  profile = SimpleProfileSerializer(read_only=True)
  likes = LikeSerializer(many=True, read_only=True)
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ['id', 'profile', 'description', 'image', 'created_at', 'likes', 'comments']
  
class ProfileSerializer(serializers.ModelSerializer):
  following = SimpleProfileSerializer(many=True, read_only =True)
  followers = SimpleProfileSerializer(many=True, read_only =True)
  posts = PostSerializer(many=True, read_only = True)
  user = UserSerializer(read_only=True)

  class Meta:
    model = Profile
    fields = '__all__'

PostSerializer.profile = ProfileSerializer(read_only=True)

