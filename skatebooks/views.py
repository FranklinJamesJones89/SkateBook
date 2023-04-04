from django.shortcuts import render

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
