from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/profile_festus/', views.profile_festus, name='profile_festus'),
    path('profile/profile_jane/', views.profile_jane, name='profile_jane'),
    path('profile/profile_peter/', views.profile_peter, name='profile_peter'),
    path('login/', views.login_view, name='login'),
    path('ambassador/', views.ambassador, name='ambassador'),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('worker/', views.worker, name='worker'),
    path('employer/', views.employer, name='employer'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('jpost',views.post_job,name='jobpost')
]
