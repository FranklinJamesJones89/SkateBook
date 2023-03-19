from django.shortcuts import render
from . models import Spot, User

# Create your views here.

def index(request):
    users = User.objects.all()
    spots = Spot.objects.all()
    context = {'spots': spots, 'users': users}
    return render(request, 'skatebooks/index.html', context)
