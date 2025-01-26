from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),  # Endpoint for retrieving all users
    path('users/create/', views.create_user, name='create_user'),  # Endpoint for creating a user
    path('tasks/', views.get_tasks, name='get_tasks'),  # Endpoint for retrieving all tasks
    path('tasks/create/', views.create_task, name='create_task'),  # Endpoint for creating a task
]