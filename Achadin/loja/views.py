from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Loja
from .forms import LojaForm
from django.urls import reverse_lazy
# Create your views here.

class DetailLoja (DetailView):
    model = Loja
    template_name = 'loja/detalhes_loja.html'
    context_object_name = 'loja'

class CreateLoja(CreateView):
    model = Loja
    template_name = 'loja/form_loja.html'
    form_class = LojaForm

class DeleteLoja(DeleteView):
    model = Loja
    template_name = 'loja/confirmar_exclusao.html'
    success_url = reverse_lazy('loja:lista')

class UpdateLoja (UpdateView):
    model = Loja
    template_name = 'form_loja.html'
    form_class = LojaForm