from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    username = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    bio = models.TextField(blank = True)
    avatar = models.ImageField(default = 'avatar.svg', blank = True, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
