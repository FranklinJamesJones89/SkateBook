from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import User, Spot
from . forms import MyUserCreationForm, SpotForm

# Create your views here.

@login_required(login_url = 'skatebooks:signup')
def index(request):
    if 'q' in request.GET:
       q = request.GET['q'] 
       #spots = Spot.objects.filter(city__icontains = q)
       multiple_q = Q(Q(city__icontains = q) | Q(state__icontains = q))
       spots = Spot.objects.filter(multiple_q)
    else:
        spots = Spot.objects.all()

    form = SpotForm()

    if request.method == 'POST':
        form = SpotForm(request.POST, request.FILES)

        if form.is_valid():
            spot = form.save(commit = False)
            spot.owner = request.user
            form.save()

            return redirect('skatebooks:index')

    context = {'spots': spots, 'form': form}

    return render(request, 'skatebooks/index.html', context)

def signin(request):
    page = 'signin'
    if request.user.is_authenticated:
        return redirect('skatebooks:index')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.info(request, 'No such email')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('skatebooks:index')
        else:
            message.info(request, 'Email or password do not exist')

    context = {'page': page}
    
    return render(request, 'skatebooks/components/forms/signup_form.html', context)

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
            
    return render(request, 'skatebooks/components/forms/signup_form.html', context)

def signout(request):
    logout(request)
    return redirect('skatebooks:index')
    
    
        


