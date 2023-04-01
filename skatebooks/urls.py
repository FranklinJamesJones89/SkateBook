from django.urls import path
from . import views

app_name = 'skatebooks'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('category/<str:pk>/', views.category, name = 'category'),
]
