from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['POST'])
@permission_classes([])
def create_user(request): 
    user = User.objects.create(username=request.data['username'])
    user.set_password(request.data['password']) 
    user.save()

    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    profile.save()

    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
  user = request.user
  profile = user.profile
  serializer = ProfileSerializer(profile, many=False)
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  post = Post.objects.create(profile=profile, description=request.data['description'], image=request.data['image'])
  post_serialized = PostSerializer(post)
  return Response(post_serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_following_posts(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   following = profile.following.all()
   posts = Post.objects.filter(profile__in=following).order_by('-created_at')
   posts_serializer = PostSerializer(posts, many=True)
   return Response(posts_serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_like_to_post(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   post = Post.objects.get(id=request.data['post_id'])
   like_exists = Like.objects.filter(profile=profile, post=post).exists()
   if not like_exists:
      Like.objects.create(profile=profile, post=post)
   serialized_post = PostSerializer(post)
   return Response(serialized_post.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_comment_to_post(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   post = Post.objects.get(id=request.data['post_id'])
   Comment.objects.create(profile=profile, post=post, text=request.data['comment'])
   serialized_post = PostSerializer(post)
   return Response(serialized_post.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile_to_see(request):
  print("***************************************************", request.query_params)
  profile = Profile.objects.get(id=request.query_params['profile_id'])
  serializer = ProfileSerializer(profile, many=False)
  return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  profile.description = request.data['bio']
  profile.profile_picture = request.data['image']
  profile.save()
  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request):
  post = Post.objects.get(id=request.data['post_id'])
  post.description = request.data['description']
  post.save()
  post_serialized = PostSerializer(post)
  return Response(post_serialized.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  post = Post.objects.get(id=request.data['post_id'])
  post.delete()
  profile.save()

  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)
