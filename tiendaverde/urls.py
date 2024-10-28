"""
URL configuration for semana11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, catalogo, form, registro, agregar_al_carrito, eliminar_del_carrito, ver_carrito, pagar_carrito, pedido
#from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('agregar/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('form/',form, name='form'),
    path('registro', registro, name="registro"),
    path('pagar/', pagar_carrito, name='pagar_carrito'),
    path('pedido/', pedido, name='pedido'),
]
