from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from app import views
from portfolio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]