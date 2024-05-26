from django.contrib import admin
from .models import Comuna, Region, Usuario, Inmueble, SolicitudArriendo

admin.site.register(SolicitudArriendo)
admin.site.register(Inmueble)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)