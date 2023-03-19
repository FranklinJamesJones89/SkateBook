from django.urls import path
from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index')
]
