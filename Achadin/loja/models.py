from django.db import models

from conta_logista.models import Logista


# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='lojas/logo/')
    banner = models.ImageField(blank=True, null=True, upload_to='lojas/banner/')
    CATEGORIAS = [
        ('r.l','Restaurantes e Lanchonetes'),
        ('mercados','Mercados'),
        ('r.c.a','Roupas, Calçados e Acessórios'),
        ('f.c','Ferramentas e Construção'),
        ('m.b','Moda e Beleza'),
        ('pet-shop', 'Pet-shop'),
        ('saude','Saúde'),
        ('m.g', 'Músicas e Games')
        ]
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    logista = models.ForeignKey(Logista, on_delete=models.CASCADE, blank=True, null=True) # ESTÁ COMO OPICIONAL PROVISÓRIAMENTE
