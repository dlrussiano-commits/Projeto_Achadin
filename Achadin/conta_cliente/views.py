from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def perfil_cliente(request):
    cliente = request.user.cliente
    return render (request, "template_mostrar_cliente.html", {"cliente":cliente})