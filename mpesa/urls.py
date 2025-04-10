from django.urls import path
from . import views


urlpatterns=[
    path('daraja',views.reg_callback,name='index')
]