from django.db import models

from loja.models import Loja


# Create your models here.

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    quantidade = models.IntegerField(null=True, blank=True)
    foto =  models.ImageField(upload_to='produtos/foto/', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='produtos', null=True)