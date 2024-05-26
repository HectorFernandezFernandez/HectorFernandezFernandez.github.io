from django import forms
from .models import Usuario, Inmueble

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'password': forms.PasswordInput(),
        }

class EdicionPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

        def clean_username(self):
            username = self.cleaned_data.get('username')
            return username
        
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = '__all__'