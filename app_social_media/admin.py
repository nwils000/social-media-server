from django.contrib import admin
from app_social_media.models import *


class ProfileAdmin(admin.ModelAdmin):
  pass

class PostAdmin(admin.ModelAdmin):
  pass




admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
