from django.contrib import admin
from .models import User, Category, Spot, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Spot)
admin.site.register(Comment)
