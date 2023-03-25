from django.urls import path

from . import views

app_name = 'skatebooks'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
    path('like-spot', views.like_spot,name ='like-spot'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('settings/', views.settings, name = 'settings'),
]
