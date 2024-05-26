from django.contrib import admin
from .models import Flan, ContactForm, Cart, CartItem
# Register your models here.

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Cart)
admin.site.register(CartItem)