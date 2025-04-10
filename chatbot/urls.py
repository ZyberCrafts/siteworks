from django.urls import path
from . import views
from .views import chat_view

urlpatterns = [
    path('get-response/', views.chatbot_response, name='chatbot_response'),
    path('chat/', chat_view, name='chat'),
]
