from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Profile, User #Profile model for roles
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
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']  # Capture the selected role

        # Create the user and associate the role
        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(user=user, role=role)

        return redirect('login')  # Redirect to the login page after registration

    return render(request, 'registration.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            
            # Retrieve the user's role from the Profile model
            profile = Profile.objects.get(user=user)
            role = profile.role

            # Redirect based on the user's role
            if role == 'Employer':
                return redirect('employer')  # URL to employer dashboard
            elif role == 'Worker':
                return redirect('worker')  # URL to worker dashboard
            elif role == 'Ambassador':
                return redirect('ambassador')  # URL to ambassador dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')