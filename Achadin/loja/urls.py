from os import name

from django.urls import path
from .views import UpdateLoja, DeleteLoja, detalhes_loja, criar_loja

urlpatterns = [
    path ('<int:pk>/detalhes/', detalhes_loja, name='detalhes'),
    path('criar/', criar_loja, name='criar'),
    path('<int:pk>/editar/', UpdateLoja.as_view(), name='editar'),
    path('<int:pk>/confirmar_exclusão', DeleteLoja.as_view(), name='confirmar_exclusao')
]