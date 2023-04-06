from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Spot, Category

# Create your views here.

def index(request):
    spots = Spot.objects.all()
    categories = Category.objects.all()

    context = {'spots': spots, 'categories': categories}

    return render(request, 'skatebooks/index.html', context)

def categories(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(id = pk)
    spots = category.spot_set.order_by('-created')

    context = {'category': category, 'spots': spots, 'categories': categories}

    return render(request, 'skatebooks/categories.html', context)

def spot(request, pk):
    spot = Spot.objects.get(id = pk)
    categories = Category.objects.all()

    context = {'spot': spot, 'categories': categories}

    return render(request, 'skatebooks/spot.html', context)

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
            messages.error(request, 'No such user')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            
            return redirect('skatebooks:index')
        else:
            messages.error(request, 'Username or email does not exist')
    
    context = {'page': page}

    return render(request, 'skatebooks/components/forms/signup_form.html', context)

def signup(request):
    form = SignupForm
    
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            print('Valid')
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            return redirect('skatebooks:index')
        else:
            messages.error(request, 'Registration Error')

    return render(request, 'skatebooks/components/forms/signup_form.html')

def signout(request):
    logout(request)

    return redirect('skatebooks:index')
