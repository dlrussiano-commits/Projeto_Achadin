from django.urls import path

from .views import Comprar, Entregando

urlpatterns = [
    path('<int:pk>/comprar/', Comprar.as_view() ,name='comprar'),
    path('entregando/', Entregando.as_view(), name='entregando')
]