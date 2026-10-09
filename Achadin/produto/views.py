from django.shortcuts import render
from django.views.generic import DetailView

from .models import Produto


# Create your views here.

class Comprar (DetailView):
    model = Produto
    template_name = 'produto/comprar_produto.html'
    context_object_name = 'produto'