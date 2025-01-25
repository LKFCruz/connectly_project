from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),  # For GET request to fetch all users
    path('users/create/', views.create_user, name='create_user'),  # For POST request to create a user
    
]