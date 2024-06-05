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

class PostSerializer(serializers.ModelSerializer):
  profile = SimpleProfileSerializer(read_only=True)

  class Meta:
    model = Post
    fields = ['profile', 'description', 'image', 'created_at']
    read_only_fields = ['profile', 'created_at']

  def create(self, validated_data):
    profile = self.context.get('profile')
    return Post.objects.create(profile=profile, **validated_data)
  
class ProfileSerializer(serializers.ModelSerializer):
  following = SimpleProfileSerializer(many=True, read_only =True)
  followers = SimpleProfileSerializer(many=True, read_only =True)
  posts = PostSerializer(many=True, read_only = True)

  class Meta:
    model = Profile
    fields = '__all__'

PostSerializer.profile = ProfileSerializer(read_only=True)

# class AllProfilePosts(serializers.ModelSerializer):
#   posts = PostSerializer(many=True, read_only=True)

#   class Meta:
#     model = Profile
#     fields = ['id', 'first_name', 'last_name', 'posts']


# class ImageSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Image
#     fields = ['id', 'title', 'image', 'created_at']