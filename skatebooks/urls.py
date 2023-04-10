from django.urls import path
from . import views

app_name = 'skatebooks'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('signout', views.signout, name = 'signout'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('categories/<str:pk>/', views.categories, name = 'categories'),
    path('spot/<str:pk>/', views.spot, name = 'spot'),
    path('like_spot', views.like_spot, name = 'like_spot'),
    path('delete_comment/<str:pk>/', views.delete_comment, name = 'delete_comment')
]
