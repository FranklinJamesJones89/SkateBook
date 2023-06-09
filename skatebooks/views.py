from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, CommentForm, SpotForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Spot, Category, LikeSpot, Comment

# Create your views here.

def index(request):
    # Queries
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
                Q(city__icontains = q) | 
                Q(state__icontains = q) |
                Q(zipcode__icontains = q) |
                Q(name__icontains = q) 
                )
        spots = Spot.objects.filter(multiple_q)
    else:
        spots = Spot.objects.all()

    categories = Category.objects.all()

    context = {'spots': spots, 'categories': categories}

    return render(request, 'skatebooks/index.html', context)

def profile(request, pk):
    user = User.objects.get(id = pk)
    spots = user.spot_set.all()

    form = SpotForm()

    context = {'user': user, 'spots': spots}

    return render(request, 'skatebooks/profile.html', context)

def categories(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(id = pk)
    spots = category.spot_set.order_by('-created')

    context = {'category': category, 'spots': spots, 'categories': categories}

    return render(request, 'skatebooks/categories.html', context)

def spot(request, pk):
    spot = Spot.objects.get(id = pk)
    spot_comments = spot.comment_set.all()
    categories = Category.objects.all()

    form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit = False)
                comment.owner = request.user
                comment.spot = spot
                form.save()
        else:
            return redirect('skatebooks:signin')

    context = {'spot': spot, 'categories': categories, 'form': form, 'spot_comments': spot_comments}

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

@login_required(login_url = 'skatebooks:signin')
def signout(request):
    logout(request)

    return redirect('skatebooks:index')

@login_required(login_url = 'skatebooks:signin')
def like_spot(request):
    username = request.user.username
    spot_id = request.GET.get('spot_id')
    spot = Spot.objects.get(id = spot_id)

    spot_filter = LikeSpot.objects.filter(username = username, spot_id = spot_id).first()

    if spot_filter == None:
        new_like = LikeSpot.objects.create(username = username, spot_id = spot_id)
        new_like.save()
        spot.num_of_likes = spot.num_of_likes + 1
        spot.save()

        return redirect('skatebooks:spot', spot_id)
    else:
        spot_filter.delete()
        spot.num_of_likes = spot.num_of_likes - 1
        spot.save()

        return redirect('skatebooks:spot', spot_id)

@login_required(login_url = 'skatebooks:signin')
def delete_comment(request, pk):
    comment = Comment.objects.get(id = pk)

    if request.user != comment.owner:
        return HttpResponse('You are not the owner')
    
    if request.method == 'POST':
        comment.delete()
       
        return redirect('skatebooks:index')

    return render(request, 'skatebooks/components/forms/delete_comment.html', {'obj': comment})

@login_required(login_url = 'skatebooks:signin')
def spot_form(request):
    form = SpotForm()

    if request.method == 'POST':
        form = SpotForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid')
            spot = form.save(commit = False)
            spot.owner = request.user
            form.save()

            return redirect('skatebooks:spot', pk=spot.id)
        else:
            print('form not valid')
    
    context = {'form': form}

    return render(request, 'skatebooks/components/forms/spot_form.html', context)

def delete_spot(request, pk):
    spot = Spot.objects.get(id = pk)

    if request.method == 'POST':
        spot.delete()

        return redirect('skatebooks:index')

    return render(request, 'skatebooks/components/forms/delete_spot.html', {'obj': spot})

@login_required(login_url = 'skatebooks:signin')
def settings(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = user)
        
        if form.is_valid():
            print('valid')
            form.save()

            return redirect('skatebooks:profile', pk = user.id)
    
    context = {'form': form} 

    return render(request, 'skatebooks/components/forms/settings.html', context)

def about(request):
    return render(request, 'skatebooks/about.html')
