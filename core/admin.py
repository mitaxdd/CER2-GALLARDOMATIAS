from django.contrib import admin
from .models import Carrera,Pedido,Producto

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Pedido)
admin.site.register(Producto)