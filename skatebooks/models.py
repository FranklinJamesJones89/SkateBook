from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True, max_length = 200)
    hometown = models.CharField(max_length = 200)
    avatar = models.ImageField(upload_to = 'img/', null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Spot(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 200)
    fuck12 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'img/', null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'spots'
