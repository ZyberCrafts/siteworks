from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your email'
    }))
    phone_number = forms.CharField(max_length=10, required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "phone_number", "password2")
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your registered email'}))