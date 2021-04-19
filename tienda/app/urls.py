from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
   path('',Home.as_view(), name='Index'),  
   path('inicio/',Home.as_view(), name='inicio'),  
   path('categorias/',Categorias.as_view(), name='categorias'),
   path('productos/<int:pk>/',Articulos.as_view(), name='productos'),
   path('info/<int:pk>/',InfoProducto.as_view(), name='infoproductos'),


 
]