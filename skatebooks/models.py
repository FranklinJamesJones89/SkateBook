from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    username = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    hometown = models.CharField(max_length = 500, blank = True, null = True)
    avatar = CloudinaryField(default = 'avatar', blank = True, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Spot(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 500)
    description = models.TextField()
    street = models.CharField(max_length = 500)
    city = models.CharField(max_length = 500)
    state = models.CharField(max_length = 500)
    zipcode = models.CharField(max_length = 500)
    twelve = models.CharField(max_length = 500)
    image = CloudinaryField()
    num_of_likes = models.IntegerField(default = 0, null = True)
    created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
    

class LikeSpot(models.Model):
    spot_id = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete = models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text[:50]
