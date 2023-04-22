from django.urls import path
from . import views

app_name = 'skatebooks'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('signout', views.signout, name = 'signout'),
    path('categories/<str:pk>/', views.categories, name = 'categories'),
    path('spot/<str:pk>/', views.spot, name = 'spot'),
    path('like_spot', views.like_spot, name = 'like_spot'),
    path('delete_comment/<str:pk>/', views.delete_comment, name = 'delete_comment'),
    path('spot_form', views.spot_form, name = 'spot_form'),
    path('delete_spot/<str:pk>/', views.delete_spot, name = 'delete_spot'),
]
