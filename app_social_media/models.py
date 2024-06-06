from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
  description = models.CharField(max_length=200)
  profile_picture = models.ImageField(upload_to='images/')


  def __str__(self):
    return self.user.username


class Post(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
  description = models.TextField(max_length=1000)
  image = models.ImageField(upload_to='images/')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.description
  
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username}"

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'post')

    def __str__(self):
        return f"{self.profile.user.username}"
