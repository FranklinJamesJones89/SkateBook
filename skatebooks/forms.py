from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Spot

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class SpotForm(ModelForm):
    class Meta:
        model = Spot
        fields = '__all__'
        exclude = ['owner']
