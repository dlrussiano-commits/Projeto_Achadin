from django.contrib import admin
from loja.models import Loja
from conta_logista.models import Logista

# Register your models here.
admin.site.register(Loja)
admin.site.register(Logista)