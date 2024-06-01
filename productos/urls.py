from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    # Crear la URL de la vista index
    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_productos, name='crear_productos'),
]
