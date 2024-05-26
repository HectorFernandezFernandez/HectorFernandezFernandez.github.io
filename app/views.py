from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def informacion(request):
    return render(request, 'about.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def formacion(request):
    return render(request, 'formacion.html')

def competencias(request):
    return render(request, 'competencias.html')

def succes(request):
    return render(request, 'succes.html')