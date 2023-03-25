from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import User, Spot, Message, LikeSpot
from . forms import MyUserCreationForm, SpotForm, ProfileForm

# Create your views here.

@login_required(login_url = 'skatebooks:signin')
def index(request):
    # Queries
    if 'q' in request.GET:
       q = request.GET['q'] 
       #spots = Spot.objects.filter(city__icontains = q)
       multiple_q = Q(Q(city__icontains = q) | Q(state__icontains = q))
       spots = Spot.objects.filter(multiple_q)
    else:
        spots = Spot.objects.all()

    form = SpotForm()
    
    #POST requests
    if request.method == 'POST':
        form = SpotForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid')
            spot = form.save(commit = False)
            spot.owner = request.user
            form.save()
        else:
            print('form is not valid')

            return redirect('skatebooks:index')

    context = {'spots': spots, 'form': form}

    return render(request, 'skatebooks/index.html', context)

def profile(request, pk):
    user = User.objects.get(id = pk)
    spots = user.spot_set.all()

    context = {'user': user, 'spots': spots}

    return render(request, 'skatebooks/profile.html', context)

def settings(request):
    user = request.user
    form = ProfileForm(instance = user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = user)
        
        if form.is_valid():
            print('valid')
            form.save()
        else:
            print('not valid')
            
            return redirect('skatebooks:profile', pk = user.id)

    
    context = {'user': user, 'form': form}

    return render(request, 'skatebooks/settings.html', context)

@login_required(login_url = 'skatebooks:signin')
def like_spot(request):
    username = request.user.username
    spot_id = request.GET.get('spot_id')
    spot = Spot.objects.get(id = spot_id)

    like_filter = LikeSpot.objects.filter(spot_id = spot_id, username = username).first()
    
    if like_filter == None:
        new_like = LikeSpot.objects.create(spot_id = spot_id, username = username)
        new_like.save()
        spot.num_of_likes = spot.num_of_likes+1
        spot.save()

        return redirect('/')
    else:
        like_filter.delete()
        spot.num_of_likes = spot.num_of_likes-1
        spot.save()

        return redirect('/')
        
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
