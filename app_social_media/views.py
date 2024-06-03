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
        # username=request.data['username']
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
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
  image_serialized = ImageSerializer(data=request.data)
  if image_serialized.is_valid():
    image_serialized.save()
    return Response(image_serialized.data, status.HTTP_201_CREATED)
  return Response(image_serialized.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
  images = Image.objects.all()
  images_serialized = ImageSerializer(images, many=True)
  return Response(images_serialized.data)
