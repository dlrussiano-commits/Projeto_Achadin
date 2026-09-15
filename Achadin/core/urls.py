from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='achadin_home'),
    path("categorias/<str:categoria>", views.exibir_categorias, name='exibir_categorias')

]