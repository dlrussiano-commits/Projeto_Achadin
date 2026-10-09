from django.shortcuts import render
from loja.models import Loja


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def exibir_categorias(request, categoria):
    lojas = Loja.objects.filter(categoria=categoria)
    categorias_dict = dict(Loja.CATEGORIAS)
    categoria_nome = categorias_dict.get(categoria)
    return render (request, 'core/exibir_categorias.html', {'lojas':lojas, 'categoria_nome':categoria_nome})
