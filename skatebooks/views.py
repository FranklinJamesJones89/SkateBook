from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Spot
from . forms import MyUserCreationForm

# Create your views here.

def index(request):
    spots = Spot.objects.all()
    context = {'spots': spots}
    return render(request, 'skatebooks/index.html', context)

def signup(request):
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            print('is valid')
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect('skatebooks:index')
        else:
            print('not valid')

    context= {'form': form}
            
    return render(request, 'skatebooks/signup_form.html', context)

