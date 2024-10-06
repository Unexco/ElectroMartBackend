from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def secret_key_view(request):
    return HttpResponse(f'SECRET_KEY is: {settings.SECRET_KEY}')

# Create your views here.
