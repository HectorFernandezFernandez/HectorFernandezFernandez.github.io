from django.shortcuts import render

# Create your views here.

def index_viajes_chile(request):
    return render(request, 'index_viajes_chile.html')