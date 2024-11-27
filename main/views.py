from django.shortcuts import render

import os
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_fixed_content_with_env(request):
    # Access the environment variable
    
    # Create a fixed content response combined with the environment variable
    response_content = {
        'fixed_message': 'This is a fixed message.',
        'env_variable': os.getenv("BONJOUR", "Not Set")  # Include the environment variable
    }
    
    # Return the response as JSON
    return JsonResponse(response_content)
