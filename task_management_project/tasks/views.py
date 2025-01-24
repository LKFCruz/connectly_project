from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, Task

# 1. Retrieve All Users (GET)
def get_users(request):
    users = list(User.objects.values('id', 'username', 'email', 'created_at'))
    return JsonResponse(users, safe=False)

# 2. Create a User (POST)
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(username=data['username'], email=data['email'])
        return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)

# 3. Retrieve All Tasks (GET)
def get_tasks(request):
    tasks = list(Task.objects.values('id', 'title', 'description', 'is_completed', 'user', 'created_at'))
    return JsonResponse(tasks, safe=False)

# 4. Create a Task (POST)
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user'])  # This assumes the user ID exists.
        task = Task.objects.create(title=data['title'], description=data.get('description', ''), user=user)
        return JsonResponse({'id': task.id, 'message': 'Task created successfully'}, status=201)