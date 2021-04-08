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
        context['productos']= Producto.objects.all()

        return context


class Tienda(ListView):
    template_name = 'app/index.html'
    queryset = Producto.objects.all()
    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productos']= Producto.objects.all()
        context['destacados']= Producto.objects.filter(destacados = True)[:3]
        context['nuevos']= Producto.objects.filter(nuevos = True)[:3]
        return context
