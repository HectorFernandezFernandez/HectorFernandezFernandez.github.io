from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from portfolio import settings
from muebles import views

urlpatterns = [
    path('index_muebles', views.index_muebles, name='index_muebles'),
    path('register_muebles/', views.register_muebles, name="register_muebles"),
    path('login_muebles/', LoginView.as_view(template_name='login_muebles.html'), name='login_muebles'),
    path('logout_muebles/', LogoutView.as_view(next_page='index_muebles'), name='logout_muebles'),
    path('inmueble/<int:id>/', views.detalle_inmueble, name='detalle_inmueble'),
    path('solicitud_arriendo/<int:id>', views.solicitud_arriendo, name='solicitud_arriendo'),
    path('usuario_muebles/<int:user_id>/', views.usuario_muebles, name='usuario_muebles'),
    path('editar_perfil/<int:user_id>', views.editar_perfil, name='editar_perfil'),
    path('inmuebles/<int:user_id>/', views.inmuebles_especificos, name='inmuebles_especificos'),
    path('inmuebles_all/', views.inmuebles_all, name='inmuebles_all'),
    path('agregar_inmueble/<int:user_id>', views.agregar_inmueble, name='agregar_inmueble'),
    path('mueble_subido', views.mueble_subido, name='mueble_subido'),
    path('editar_inmueble/<int:id>/<int:user_id>/', views.editar_inmueble, name='editar_inmueble'),
    path('borrar_inmueble/<int:id>/', views.borrar_inmueble, name='borrar_inmueble'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)