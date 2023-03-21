from django.shortcuts import render
from .models import User, Spot

# Create your views here.

def index(request):
    spots = Spot.objects.all()
    context = {'spots': spots}
    return render(request, 'skatebooks/index.html', context)

