from django.db import models
class Carrera(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    nombre = models.CharField(max_length=60)
    duracion = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    
class Pedido(models.Model):

    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=60, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')], default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    productos = models.TextField(default='')
    
    def __str__(self) -> str:
        return self.nombre
    
    def calcular_total(self):
        total = 0
        for item in self.productos.split(','):
            producto_id, cantidad = item.split(':')
            producto = Producto.objects.get(id=producto_id)
            total += producto.precio * int(cantidad)
        self.total = total
        self.save()

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    precio=models.IntegerField()
    imagen = models.ImageField(upload_to='static/core/img/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nombre
