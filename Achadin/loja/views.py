from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Loja
from .forms import LojaForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.


def detalhes_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    return render (request, 'loja/detalhes_loja.html', {'loja':loja})



def criar_loja(request):
    if request.method == 'POST':
        form = LojaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('achadin_home')
    else:
        form = LojaForm()
    return render (request, 'loja/form_loja.html', {'form':form})


class DeleteLoja(DeleteView):
    model = Loja
    template_name = 'loja/confirmar_exclusao.html'
    # success_url = reverse_lazy('loja:lista')

class UpdateLoja (UpdateView):
    model = Loja
    template_name = 'form_loja.html'
    form_class = LojaForm