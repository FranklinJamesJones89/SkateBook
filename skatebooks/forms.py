from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Spot, Message

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class SpotForm(ModelForm):
    class Meta:
        model = Spot
        fields = '__all__'
        exclude = ['owner', 'num_of_likes']

class CommentForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['user', 'spot']

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'name', 'email', 'bio', 'hometown']

