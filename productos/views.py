from django.shortcuts import render,  get_object_or_404, redirect
from .models import Producto

productos = []

def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request,'listar.html',{'productos':productos})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.nombre = request.POST.get('nombre', '')
        producto.precio = float(request.POST.get('precio', 0))
        producto.cantidad = int(request.POST.get('cantidad', 0))
        producto.save()
        return redirect('listar_productos')
    return render(request, 'editar.html', {'producto': producto})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')