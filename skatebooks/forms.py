from .models import User, Comment
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
