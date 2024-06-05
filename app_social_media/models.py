from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.TextField()
  last_name = models.TextField()
  following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

  def __str__(self):
    return self.user.username


class Post(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
  description = models.TextField(max_length=1000)
  image = models.ImageField(upload_to='images/')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.description