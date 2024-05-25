from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('fashion/', views.fashion, name='fashion'),
    path('about/', views.about, name='about'),
    path('photography/', views.photography, name='photography'),
    path('travel/', views.travel, name='travel'),
    path('single/', views.single, name='single'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])