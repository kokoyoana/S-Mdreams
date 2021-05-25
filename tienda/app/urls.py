from django.urls import path
from .views import *

urlpatterns = [
    path('', Portada.as_view(), name='portada'),
    path('producto/<int:pk>', InfoProducto.as_view(), name='producto'),
    path('carrito', Carrito.as_view(), name='carrito'),
    path('carrito/agregar/<int:pk>', carrito_agregar, name='carrito_agregar'),
    path('carrito/eliminar/<int:pk>', carrito_eliminar, name='carrito_eliminar'),

    path('inicio/', Inicio.as_view(), name='inicio'),
    path('categorias/', Categorias.as_view(), name='categorias'),
    path('productos/<int:pk>/', Articulos.as_view(), name='productos'),
    path('info/<int:pk>/', InfoProducto2.as_view(), name='infoproductos'),
]