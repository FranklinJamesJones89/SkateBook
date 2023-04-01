from django.shortcuts import render

from .models import User, Spot, Category

# Create your views here.

def index(request):
    spots = Spot.objects.all()
    categories = Category.objects.all()

    context = {'spots': spots, 'categories': categories}

    return render(request, 'skatebooks/index.html', context)

def category(request, pk):
    spots = Spot.objects.get(id = pk)
    spot = spots.category_set.all()

    context = {'spot': spot}

    return render(request, 'skatebooks/category', context)
