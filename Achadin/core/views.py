from django.shortcuts import render
from loja.models import Loja


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def exibir_categorias(request, categoria):
    lojas = Loja.objects.filter(categoria=categoria)
    return render (request, 'core/exibir_categorias.html', {'lojas':lojas})
