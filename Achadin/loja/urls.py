from os import name

from django.urls import path
from .views import DetailLoja, UpdateLoja, CreateLoja, DeleteLoja

urlpatterns = [
    path ('<int:pk>/detalhes/', DetailLoja.as_view(), name='detalhes'),
    path('criar/', CreateLoja.as_view(), name='criar'),
    path('<int:pk>/editar/', UpdateLoja.as_view(), name='editar'),
    path('<int:pk>/confirmar_exclusão', DeleteLoja.as_view(), name='confirmar_exclusao')


]