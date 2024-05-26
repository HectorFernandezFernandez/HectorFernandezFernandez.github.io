from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('success/', views.succes, name='success'),
    path('formacion/', views.formacion, name='formacion'),
    path('informacion/', views.informacion, name='informacion'),
    path('competencias/', views.competencias, name='competencias'),
    path('onlyflans/', include('flanes.urls')),
    path('muebles/', include('muebles.urls')),
    path('viajes_chile/', include('viajes_chile.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])