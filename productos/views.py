from django.shortcuts import render
from .models import Producto

productos = []

def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request,'listar.html',{'productos':productos})