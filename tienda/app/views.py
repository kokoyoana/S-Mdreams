from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from django.views.generic import *
from .models import *
from django.http import HttpResponseRedirect
from django.forms import MultipleChoiceField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from random import choices
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.

def inicializar_productos():
    resultado = {}
    categorias = Categoria.objects.all()
    for categoria in categorias:
        productos = categoria.producto_set
        resultado[categoria] = productos.all()

    print(resultado)
    return resultado
    




class Home(TemplateView):
    template_name='app/index.html'


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)


        context['infopro'] = inicializar_productos()
        #context['categorias']= Categoria.objects.all()
        #context['productos']= Producto.objects.all() 
        context['destacados']= Producto.objects.filter(destacados = True)[:3]
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        context['algunos']= Producto.objects.filter(algunos = True)[:6]

        return context






class Categorias(ListView):
    template_name = 'app/index.html'
    context_object_name= 'categorias' 
    queryset = Categoria.objects.all()
    model = Categoria
    
    def get_context_data(self,**kwargs):
        context=super(Categorias, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)
        context['infopro'] = Categoria.objects.filter(categoria=idSer)
        context['productos'] = Producto.objects.all()
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        context['algunos']= Producto.objects.filter(algunos = True)[:6]
        context['destacados']= Producto.objects.filter(destacados = True)[:3]


        return context



class Articulos(TemplateView):
    template_name = 'app/index.html'
    context_object_name= 'productos' 
    model = Producto
    
    def get_context_data(self,**kwargs):
        context=super(Articulos, self).get_context_data(**kwargs)
        idPro = self.kwargs.get('pk',None)
        context['infopro'] = Categoria.objects.filter(categoria=idPro)
        print(idPro)
        print(context['infopro'])

        context['categorias']= Categoria.objects.all()
        context['productos'] = Producto.objects.all()
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        context['algunos']= Producto.objects.filter(algunos = True)[:6]
        context['destacados']= Producto.objects.filter(destacados = True)[:3]


        return context
