from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Profile,Job 
from django.core.mail import send_mail   
from .forms import ForgotPasswordForm     
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator    
from django.contrib.auth.hashers import make_password   
from django.http import JsonResponse
from .utils import create_email_campaign
from sib_api_v3_sdk import Configuration, ApiClient, TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail
from sib_api_v3_sdk.rest import ApiException 
from django.http import HttpResponse
import datetime
  
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
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def profile_festus(request):
    return render(request, 'profile_festus.html')
def profile_jane(request):
    return render(request, 'profile_jane.html')
def profile_peter(request):
    return render(request, 'profile_peter.html')
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
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
            return redirect('login')
        else:
            return render(request, 'registration.html', {'error': 'Please fill all the fields correctly.'})

    return render(request, 'registration.html')
def login_view(request):
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

token_generator = PasswordResetTokenGenerator()

# def forgot_password(request):
#     if request.method == 'POST':
#         form = ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 # Generate a password reset token and link
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = token_generator.make_token(user)
#                 reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')
#                     # Send the email
#                 send_mail(
#                     'Password Reset Request',
#                     f'Click the link to reset your password: {reset_link}',
#                     'request.user.email',  # Sender email
#                     [email],  # Recipient email
#                     fail_silently=False,
#                 )
#                 return render(request, 'forgot_password_sent.html', {'email': email})
#             except User.DoesNotExist:
#                 return render(request, 'forgot_password.html', {'error': 'No account with this email exists. Please enter a valid email Account'})
#     else:
#         form = ForgotPasswordForm()
#     return render(request, 'forgot_password.html', {'form': form})
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the form
        try:
            user = User.objects.get(email=email)  # Check if the user exists
            # Generate a unique token and reset link
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_link = f"http://127.0.0.1:8000/reset-password/{uid}/{token}/"

            # Send password reset email using Brevo API
            configuration = Configuration()
            #configuration.api_key['api-key'] = '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'  # Replace with your Brevo API key
            api_instance = TransactionalEmailsApi(ApiClient(configuration))

            # Define the email content
            send_smtp_email = SendSmtpEmail(
                to=[{"email": email}],
                sender={"email": "your_email@example.com", "name": "Siteworks Support"},
                subject="Password Reset Request",
                html_content=f"""
                <p>Hi {user.username},</p>
                <p>You requested to reset your password. Click the link below to reset it:</p>
                <a href="{reset_link}">Reset Password</a>
                <p>If you did not make this request, you can ignore this email.</p>
                """
            )

            # Send the email
            api_instance.send_transac_email(send_smtp_email)
            return render(request, 'forgot_password_sent.html', {'email': email})
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': 'No account found with this email.'})
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            return render(request, 'forgot_password.html', {'error': 'An error occurred. Please try again later.'})
    return render(request, 'forgot_password.html')
def reset_password(request, uidb64, token):
    try:
        user_id = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
    except (ValueError, TypeError, User.DoesNotExist):
        user = None

    if user and token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                return render(request, 'reset_password_success.html')
            else:
                return render(request, 'reset_password.html', {'error': 'Passwords do not match.'})
        return render(request, 'reset_password.html')
    else:
        return render(request, 'invalid_reset_link.html')
def create_campaign_view(request):
    api_key = "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"
    campaign_name = "password_forget"
    subject = "Password Recovery"
    sender_name = "Festus"
    sender_email = "festusonwonga@gmail.com"
    html_content = "This is a campaign sent via Brevo API."
    list_ids = [2, 7]
    scheduled_time = "2025-01-01 00:00:01"

    create_email_campaign(api_key, campaign_name, subject, sender_name, sender_email, html_content, list_ids, scheduled_time)
    return JsonResponse({"status": "Campaign created successfully!"})

def post_job(request):
    if request.user.is_authenticated:
        category=request.POST.get('category')
        description=request.POST.get('workload')
        location=request.POST.get('location')
        budget=request.POST.get('price')
        date=request.POST.get('deadlineDate')
        time=request.POST.get('deadlineTime')
        posted_date=datetime.datetime(int(date[0:4]),int(date[5:7]),int(date[8:]),int(time[0:2]),int(time[3:]))
        user=request.user
        contact=request.POST.get('contact')
        job=Job(category=category,description=description,location=location,budget=budget,
                posted_date=posted_date,employer=user,contact=contact)
        job.save()
        return render(request,'employer.html')