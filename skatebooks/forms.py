from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
