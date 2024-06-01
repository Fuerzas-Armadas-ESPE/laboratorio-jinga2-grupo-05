from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    # Crear la URL de la vista index
    path('',views.listar_productos, name='listar_productos'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:id>/', views.eliminar_producto, name='borrar_producto'),

]