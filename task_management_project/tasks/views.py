from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, Task

# Retrieve All Users
def get_users(request):
    users = list(User.objects.values('id', 'username', 'email', 'created_at'))
    return JsonResponse(users, safe=False)

# Create a User
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create(username=data['username'], email=data['email'])
            return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Retrieve All Tasks
def get_tasks(request):
    tasks = list(Task.objects.values('id', 'title', 'description', 'is_completed', 'user_id', 'created_at'))
    return JsonResponse(tasks, safe=False)

# Create a Task
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.get(id=data['user'])
            task = Task.objects.create(
                title=data['title'], 
                description=data.get('description', ''), 
                user=user
            )
            return JsonResponse({'id': task.id, 'message': 'Task created successfully'}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)