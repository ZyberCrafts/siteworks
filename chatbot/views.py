from django.shortcuts import render
import json
import os
import requests
from django.conf import settings
from django.http import JsonResponse

def chat_view(request):
    return render(request, 'chat_template.html')

def load_training_data():
    # Build the path to the JSON file
    json_path = os.path.join(settings.BASE_DIR, 'chatbot', 'data', 'responses.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def chatbot_response(request):
    # Get user message from GET parameter; convert to lowercase for matching
    user_message = request.GET.get('message', '').lower()

    # Determine user role:
    # If the user is authenticated, you might fetch it from user.profile.role.
    # For this example, we check a GET parameter named "role" (if not provided, we use 'default').
    role = request.GET.get('role', 'default')

    training_data = load_training_data()

    # Loop through each intent in training data
    for intent, content in training_data.items():
        # Check intents with examples (skip fallback since it doesn’t have "examples")
        if "examples" in content:
            # If any of the sample phrases appears in the message
            if any(example in user_message for example in content["examples"]):
                # Get the role‑specific response if available; otherwise, use the default response
                response_dict = content["response"]
                response_text = response_dict.get(role, response_dict.get("default"))
                return JsonResponse({"response": response_text})

    # If no intent matches, return the fallback response
    fallback = training_data.get("fallback", {"response": "Sorry, I couldn't understand that."})
    return JsonResponse({"response": fallback["response"]})
def chatbot_response(request):
    user_message = request.GET.get('message', '')
    role = request.GET.get('role', 'default')
    flask_url = 'http://127.0.0.1:5000/get-response'
    response = requests.get(flask_url, params={'message': user_message, 'role': role})
    data = response.json()
    return JsonResponse(data)

