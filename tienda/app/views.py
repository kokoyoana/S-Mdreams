from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import *

# from django.contrib.contenttypes.models import ContentType
# from django.http import HttpResponseRedirect
# from django.forms import MultipleChoiceField
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from random import choices
# from django.db.models import Avg
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from pprint import pprint

from .models import *
from .carro import Carro

class Portada(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super(Portada, self).get_context_data(**kwargs)
        context['destacados'] = Producto.objects.filter(destacados=True)[:4]
        context['nuevos'] = Producto.objects.filter(nuevos=True)[:4]
        context['algunos'] = Producto.objects.filter(algunos=True)[:8]
        # context['portada'] = Producto.objects.filter(portada=True)[:4]
        return context


class InfoProducto(DetailView):
    template_name = 'app/producto.html'
    model = Producto

    def get_context_data(self, **kwargs):
        idProducto = self.kwargs.get('pk', None)

        context = super(InfoProducto, self).get_context_data(**kwargs)
        context['producto'] = Producto.objects.get(id=idProducto)
        return context


class Carrito(TemplateView):
    template_name = 'app/carrito.html'

    def get_context_data(self, **kwargs):
        carro = Carro(self.request)

        context = super(Carrito, self).get_context_data(**kwargs)
        context['carro'] = carro
        return context


def carrito_agregar(request, pk):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=pk)
    carro.add(producto=producto)
    return redirect('app:carrito')


def carrito_eliminar(request, pk):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=pk)
    carro.remove(producto)
    return redirect('app:carrito')


# ======== OLD


def inicializar_productos():
    resultado = {}
    categorias = Categoria.objects.all()
    for categoria in categorias:
        productos = categoria.producto_set
        resultado[categoria] = productos.all()
    return resultado

class Inicio(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        # idSer = self.kwargs.get('pk',None)

        context['infopro'] = inicializar_productos()
        #context['categorias'] = Categoria.objects.all()
        #context['productos'] = Producto.objects.all() 
        context['destacados'] = Producto.objects.filter(destacados=True)[:4]
        context['nuevos'] = Producto.objects.filter(nuevos=True)[:4]
        context['algunos'] = Producto.objects.filter(algunos=True)[:8]
        context['portada'] = Producto.objects.filter(portada=True)[:4]

        return context

class Categorias(ListView):
    template_name = 'app/index.html'
    context_object_name = 'categorias' 
    queryset = Categoria.objects.all()
    model = Categoria

    def get_context_data(self,**kwargs):
        context = super(Categorias, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)
        context['infopro'] = Categoria.objects.filter(id=idSer)
        context['infopro'] = inicializar_productos()
        context['productos'] = Producto.objects.all()
        context['nuevos'] = Producto.objects.filter(nuevos=True)[:4]
        context['algunos'] = Producto.objects.filter(algunos=True)[:8]
        context['destacados'] = Producto.objects.filter(destacados=True)[:4]
        context['portada'] = Producto.objects.filter(portada=True)[:4]

        return context

class Articulos(TemplateView):
    template_name = 'app/index.html'
    context_object_name= 'productos' 
    model = Producto
    
    def get_context_data(self,**kwargs):
        context = super(Articulos, self).get_context_data(**kwargs)
        idPro = self.kwargs.get('pk',None)
        context['infopro'] = Categoria.objects.filter(categoria=idPro)
        context['categorias']= Categoria.objects.all()
        context['infopro'] = inicializar_productos()
        context['productos'] = Producto.objects.all()
        context['nuevos'] = Producto.objects.filter(nuevos=True)[:4]
        context['algunos'] = Producto.objects.filter(algunos=True)[:8]
        context['destacados'] = Producto.objects.filter(destacados=True)[:4]
        context['portada'] = Producto.objects.filter(portada=True)[:4]

        return context

class InfoProducto2(DetailView):
    template_name = 'app/infoproducto.html'
    model = Producto

    def get_context_data(self,**kwargs):
        context = super(InfoProducto2, self).get_context_data(**kwargs)
        idCur = self.kwargs.get('pk',None)
        context['infoproducto'] = Producto.objects.get(pk=idCur)
        context['categorias'] = Categoria.objects.all()
        context['infopro'] = inicializar_productos()
        context['productos'] = Producto.objects.all()
        context['nuevos'] = Producto.objects.filter(nuevos=True)[:4]
        context['algunos'] = Producto.objects.filter(algunos=True)[:8]
        context['destacados'] = Producto.objects.filter(destacados=True)[:4]
        context['portada'] = Producto.objects.filter(portada=True)[:4]

        return context
