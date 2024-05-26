from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje'
        }
# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(label='correo')
#     customer_name = forms.CharField(max_length=64, label='nombre')
#     message = forms.CharField(label='message')