from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def informacion(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

def formacion(request):
    return render(request, 'formacion.html')

def competencias(request):
    return render(request, 'competencias.html')