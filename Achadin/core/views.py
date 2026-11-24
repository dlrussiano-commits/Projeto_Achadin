from django.db.models import Q
from django.shortcuts import render
from loja.models import Loja
from produto.models import Produto


def home(request):
    return render(request, 'core/home.html')


def exibir_categorias(request, categoria):
    lojas = Loja.objects.filter(categoria=categoria)
    categorias_dict = dict(Loja.CATEGORIAS)
    categoria_nome = categorias_dict.get(categoria)
    return render(request, 'core/exibir_categorias.html', {'lojas': lojas, 'categoria_nome': categoria_nome})


def buscar(request):
    termo = request.GET.get('q', '').strip()
    produtos = Produto.objects.none()
    if termo:
        produtos = Produto.objects.filter(
            Q(nome__icontains=termo) | Q(descricao__icontains=termo)
        ).select_related('loja')
    return render(request, 'core/buscar.html', {'produtos': produtos, 'termo': termo})