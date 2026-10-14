from django.urls import path

from .views import Comprar, Entregando, CriarProduto

urlpatterns = [
    path('<int:pk>/comprar/', Comprar.as_view() ,name='comprar'),
    path('entregando/', Entregando.as_view(), name='entregando'),
    path('criar_produto/', CriarProduto.as_view(), name='criar_produto')
]