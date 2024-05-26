from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from muebles.models import SolicitudArriendo, Inmueble, Usuario, Comuna
from .forms import RegistroUsuarioForm, EdicionPerfilForm, InmuebleForm

def index_muebles(request):
    return render(request, 'index_muebles.html')

def inmuebles_all(request):
    inmubles = Inmueble.objects.all()
    return render(request, 'inmuebles_all.html', {'inmuebles':inmubles})

@login_required
def detalle_inmueble(request, id):
    inmueble = Inmueble.objects.get(pk=id)
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})

def register_muebles(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()
            usuario_autenticado = authenticate(username=usuario.username, password=password)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('index_muebles')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register_muebles.html', {'form': form})

@login_required
def solicitud_arriendo(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    if request.user.is_authenticated and request.user.usuario.tipo_usuario == 'arrendatario':
        if request.method == 'POST':
            form = SolicitudArriendo(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.arrendatario = request.user.usuario
                solicitud.inmueble = inmueble
                solicitud.save()
                return redirect('detalle', id=inmueble.id)
        else:
            form = SolicitudArriendo(initial={'inmueble': inmueble})
        return render(request, 'generar_solicitud_arriendo.html', {'form': form})
    else:
        return redirect('index_muebles')

@login_required
def usuario_muebles(request, user_id):
    try:
        usuario = Usuario.objects.get(id=user_id)
    except Usuario.DoesNotExist:
        if user_id == 1:
            messages.warning(request, "Problemas especificos con usuario admin, use otro.")
            return redirect('index_muebles')
        messages.warning(request, "El usuario no existe")
        return redirect('index_muebles')
    
    return render(request, 'usuario_muebles.html', {'usuario': usuario})

def editar_perfil(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        formulario = EdicionPerfilForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario_muebles', user_id=user_id)
    else:
        formulario = EdicionPerfilForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'formulario': formulario, 'usuario': usuario})

@login_required
def inmuebles_especificos(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    inmuebles = Inmueble.objects.filter(propietario=usuario)

    return render(request, 'inmuebles.html', {'inmuebles': inmuebles})

@login_required
def agregar_inmueble(request, user_id):
    comunas = Comuna.objects.all()
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = usuario
            if 'imagen' in request.FILES:
                inmueble.imagen = request.FILES['imagen']
                inmueble.save()
                return redirect('mueble_subido') 
            else:
                form = InmuebleForm()
    else:
        form = InmuebleForm()
    
    return render(request, 'agregar_inmueble.html', {'form': form, 'comunas': comunas, 'usuario': usuario})


def mueble_subido(request):
    return render(request, 'mueble_subido.html')

@login_required
def editar_inmueble(request, id, user_id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    usuario = get_object_or_404(Usuario, pk=user_id)

    if usuario.tipo_usuario == "arrendatario":
        if user_id == inmueble.propietario_id:
            if request.method == 'POST':
                form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
                if form.is_valid():
                    inmueble = form.save(commit=False)
                    inmueble.propietario = usuario
                    if 'imagen' in request.FILES:
                        inmueble.imagen = request.FILES['imagen']
                    inmueble.save()
                    return redirect('detalle_inmueble', id=inmueble.id)
            else:
                form = InmuebleForm(instance=inmueble)

            return render(request, 'editar_inmueble.html', {'form': form, 'inmueble': inmueble})
        else:
            messages.warning(request, "Solo los dueños del inmueble pueden editarlo.")
            return redirect('index_muebles')
    else:
        messages.warning(request, "Solo los dueños del inmueble pueden editarlo.")
        return redirect('index_muebles')
    
def borrar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    inmueble.delete()
    return redirect('index_muebles') 
