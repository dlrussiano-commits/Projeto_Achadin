from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, CreateView
from .forms import ProdutoForm
from django.urls import reverse_lazy

from .models import Produto


# Create your views here.

class Comprar (DetailView):
    model = Produto
    template_name = 'produto/comprar_produto.html'
    context_object_name = 'produto'

class Entregando (TemplateView):
    template_name = 'produto/entregando.html'

class CriarProduto (CreateView):
    template_name = 'produto/criar_produto.html'
    form_class = ProdutoForm
    success_url = reverse_lazy("achadin_home")