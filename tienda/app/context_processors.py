from .models import *
from .carro import Carro

def base(request):
    carro = Carro(request)
    menu = {}
    categorias = Categoria.objects.all()
    for categoria in categorias:
        productos = categoria.producto_set
        menu[categoria] = productos.all()

    return {
        'menu': menu,
        'total_productos': carro.__len__
    }
