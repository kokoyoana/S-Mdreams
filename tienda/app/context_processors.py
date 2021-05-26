from .models import *
from .carro import Carro
from django.conf import settings

def base(request):
    site_name = settings.APP_NAME
    carro = Carro(request)
    menu = {}
    categorias = Categoria.objects.all()
    for categoria in categorias:
        productos = categoria.producto_set
        menu[categoria] = productos.all()

    return {
        'site_name': site_name,
        'menu': menu,
        'total_productos': carro.__len__
    }
