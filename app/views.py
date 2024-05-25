from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def fashion(request):
    return render(request, 'fashion.html')

def photography(request):
    return render(request, 'photography.html')

def travel(request):
    return render(request, 'travel.html')

def single(request):
    return render(request, 'single.html')