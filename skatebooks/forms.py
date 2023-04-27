from .models import User, Comment, Spot
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= '__all__'
        exclude = ['owner', 'spot']

class SpotForm(ModelForm):
    class Meta:
        model = Spot
        exclude = ['owner']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'hometown', 'avatar']
        
