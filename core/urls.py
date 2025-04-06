from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('ambassador/', views.ambassador, name='ambassador'),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('worker/', views.worker, name='worker'),
    path('employer/', views.employer, name='employer'),
    
]
