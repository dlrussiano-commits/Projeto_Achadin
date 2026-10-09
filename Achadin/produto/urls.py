from django.urls import path

from .views import Comprar

urlpatterns = [
    path('<int:pk>/comprar/', Comprar.as_view() ,name='comprar')
]