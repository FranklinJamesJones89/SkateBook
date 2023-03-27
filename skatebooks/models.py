from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null = True)
    hometown = models.CharField(max_length = 200, null = True)
    avatar = models.ImageField(null = True, default = 'blank-profile-picture.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Spot(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    description = models.TextField(null = True)
    street = models.TextField(null = True)
    city = models.TextField(null = True)
    state = models.TextField(null = True)
    zipcode = models.TextField(null = True)
    fuck12 = models.TextField(null = True) 
    image = models.ImageField(null = True)
    num_of_likes = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[:50]

class LikeSpot(models.Model):
    spot_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length = 200)
    user = models.CharField(max_length = 200)

    def __str__(self):
        return self.user
