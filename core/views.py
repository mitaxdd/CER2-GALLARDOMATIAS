from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Pedido


# Create your views here.
def registro(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogo")
    form=UserCreationForm()
    return render(request, 'core/registro.html', {"form":form})

def home(request):

    productos = Producto.objects.all()
    return render(request,'core/index.html',{'productos': productos})

def agregar_al_carrito(request):
    carrito = request.session.get('carrito', {})

    if request.method == 'POST':
        producto_id = str(request.POST.get('producto_id'))
        if producto_id in carrito:
            carrito[producto_id] += 1
        else:
            carrito[producto_id] = 1

        request.session['carrito'] = carrito
        return JsonResponse({'success': True})

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if producto_id in carrito:
        del carrito[producto_id]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    carrito_items = []

    for producto in productos:
        carrito_items.append({
            'producto': producto,
            'cantidad': carrito[str(producto.id)],
            'subtotal': producto.precio * carrito[str(producto.id)]
        })

    total = sum(item['subtotal'] for item in carrito_items)
    return render(request, 'core/carrito.html', {'carrito_items': carrito_items, 'total': total})

def pagar_carrito(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        return redirect('ver_carrito')

    productos_str = ','.join(f"{producto_id}:{cantidad}" for producto_id, cantidad in carrito.items())

    pedido = Pedido.objects.create(
        nombre=request.POST.get('nombre'),
        direccion=request.POST.get('direccion'),
        estado='pendiente',
        productos=productos_str
    )

    request.session['carrito'] = {}

    return redirect('pedido', id=pedido.id)

def pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    productos = []
    for item in pedido.productos.split(','):
        producto_id, cantidad = item.split(':')
        producto = Producto.objects.get(id=producto_id)
        productos.append({'producto': producto, 'cantidad': int(cantidad)})

    return render(request, 'core/pedido.html', {'pedido': pedido, 'productos': productos})


def form(request):
    
    return render(request,'core/form.html')

def catalogo(request):
    
    return render(request,'core/catalogo.html')
