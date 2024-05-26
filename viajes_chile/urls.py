from django.urls import path
from viajes_chile import views

urlpatterns = [
    path('index_viajes_chile', views.index_viajes_chile, name='index_viajes_chile'),
]