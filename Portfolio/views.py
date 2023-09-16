from django.shortcuts import render, redirect
from .models import Contact

# def (request):
#     return render(request, 'home.html')

def index(request):
    return render (request,'index.html')

def contact(request):
    return render(request,'contact.html')


