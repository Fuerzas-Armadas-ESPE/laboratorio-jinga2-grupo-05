from django.shortcuts import render, redirect
from .models import Producto

productos = []


def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})


def crear_productos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = float(request.POST['precio'])
        cantidad = int(request.POST['cantidad'])
        producto = Producto(nombre=nombre, precio=precio,
                            cantidad=cantidad)
        producto.save()
        return redirect('listar_productos')
    return render(request, 'create.html')
