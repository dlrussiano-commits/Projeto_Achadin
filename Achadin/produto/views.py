from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Produto


# Create your views here.

class Comprar (DetailView):
    model = Produto
    template_name = 'produto/comprar_produto.html'
    context_object_name = 'produto'

class Entregando (TemplateView):
    template_name = 'produto/entregando.html'