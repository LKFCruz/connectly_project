from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.db import IntegrityError

# Create User
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            # Extract user data from the request
            import json
            data = json.loads(request.body)  # Parse raw JSON body
            username = data['username']
            email = data['email']

            # Create a new user
            user = User.objects.create(username=username, email=email)

            # Return a success response
            return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)

        except IntegrityError:
            # Handle the case where the email already exists
            return JsonResponse({'error': 'User with this email already exists.'}, status=400)

        except KeyError as e:
            # Handle the case where required fields are missing
            return JsonResponse({'error': f"'{e.args[0]}' is required"}, status=400)

# Get all Users
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()  # Fetch all users
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return JsonResponse({'users': user_list}, status=200)
