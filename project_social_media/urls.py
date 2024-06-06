from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_social_media.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', create_user),
    path('create-post/', create_post),
    path('profile/', get_profile),
    path('get-following-posts/', get_following_posts),
    path('add-like-to-post/', add_like_to_post),
    path('add-comment-to-post/', add_comment_to_post),
    path('get-profile-to-see/', get_profile_to_see),
    path('update-profile/', update_profile),
    path('update-post/', update_post),
    path('delete-post/', delete_post),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
]

# This is to see if we're runnign locally or in production
if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)