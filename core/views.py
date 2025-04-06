from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Profile
def home (request):
    return render(request, 'home.html')
def signin (request):
    return render(request, 'login.html')
def ambassador(request):
    return render(request, 'ambassador.html')
def employer(request):
    return render(request, 'employer.html')
def worker(request):
    return render(request, 'worker.html')
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        
        if password != confirm_password:
            return render(request, 'registration.html', {'error': 'Passwords do not match'})

        # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {'error': 'Username already exists. Please choose a different username.'})
        if User.objects.filter(email=email).exists():
                return render(request, 'registration.html', {'error': 'Email already exists. Please use a different email address.'})
        # Ensure all required fields are filled
        if username and email and password and role:
            user = User.objects.create_user(username=username, email=email, password=password)  # Create User object
            Profile.objects.create(user=user, role=role)  # Create associated Profile

            # Redirect to login page after successful registration
            return redirect('login')  # Replace 'login' with the name of your login URL
        else:
            return render(request, 'registration.html', {'error': 'Please fill all the fields correctly.'})

    return render(request, 'registration.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Retrieve the user's role from the Profile model
            profile = Profile.objects.get(user=user)
            role = profile.role

            # Redirect based on the role
            if role == 'Employer':
                return render(request, 'employer.html', {'user': user, 'role': role})  # Load employer.html
            elif role == 'Worker':
                return render(request, 'worker.html', {'user': user, 'role': role})  # Load worker.html
            elif role == 'Ambassador':
                return render(request, 'ambassador.html',  {'user': user, 'role': role})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')