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
class Home(TemplateView):
    template_name='app/index.html'


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)
        context['especialidad'] = Producto.objects.filter(categoria_id=idSer)
        context['categorias']= Categoria.objects.all()
        context['productos']= Producto.objects.all()
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
        context['especialidad'] = Producto.objects.filter(producto_id=idSer)
        context['productos'] = Producto.objects.all()
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        context['algunos']= Producto.objects.filter(algunos = True)[:6]
        context['destacados']= Producto.objects.filter(destacados = True)[:3]


        return context



class Articulos(TemplateView):
    template_name = 'app/index.html'
    context_object_name= 'productos' 
    queryset = Producto.objects.all()
    model = Producto
    
    def get_context_data(self,**kwargs):
        context=super(Articulos, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)
        context['infopro'] = Producto.objects.filter(categoria_id=idSer)
        context['categorias']= Categoria.objects.all()
        context['productos'] = Producto.objects.all()
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        context['algunos']= Producto.objects.filter(algunos = True)[:6]
        context['destacados']= Producto.objects.filter(destacados = True)[:3]


        return context
