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
  post_serialized = PostSerializer(data=request.data, context={'profile': profile})
  if post_serialized.is_valid():
     post_serialized.save()
     return Response(post_serialized.data, status.HTTP_201_CREATED)
  return Response(post_serialized.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_following_posts(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   following = profile.following.all()
   posts = Post.objects.filter(profile__in=following).order_by('-created_at')
   posts_serializer = PostSerializer(posts, many=True)
   return Response(posts_serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_posts(request):
#    user = request.user
#    profile = Profile.objects.get(user=user)
#    print("*******************************************", )
#    profile_serializer = ProfileSerializer(profile, many=False)
#    return Response(profile_serializer.data)

