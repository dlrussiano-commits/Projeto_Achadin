from django.contrib import admin
from loja.models import Loja
from conta_logista.models import Logista
from produto.models import Produto
from conta_cliente.models import Cliente

# Register your models here.
admin.site.register(Loja)
admin.site.register(Logista)
admin.site.register(Produto)
admin.site.register(Cliente)