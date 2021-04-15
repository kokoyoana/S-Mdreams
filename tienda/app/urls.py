from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
   path('',Home.as_view(), name='Index'),  
   path('inicio/',Home.as_view(), name='inicio'),  
   path('producto/',Tienda.as_view(), name='producto'), 
   path('categorias/', Categorias.as_view(), name='categorias'),
 
]