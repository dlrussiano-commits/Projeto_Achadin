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
    CORES = [
        ('r', 'Vermelho'),
        ('b', 'Azul'),
        ('y', 'Amarelo'),
        ('g', 'Verde'),
        ('p', 'Rosa'),
        ('o','Laranja'),
        ('db', 'Azul Escuro')

    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    cores = models.CharField(max_length=20, choices=CORES)
    ESTILOS = [('solido', 'Sólido'), ('contorno', 'Contorno'), ('redondo', 'Arredondado')]
    HEX = {'r': '#e53935', 'b': '#1976f3', 'y': '#fdd835', 'g': '#43a047',
           'p': '#ec407a', 'o': '#fb8c00', 'db': '#0d2a6b'}

    estilo_botao = models.CharField(max_length=10, choices=ESTILOS, default='solido')
    texto_banner = models.CharField(max_length=80, blank=True)

    @property
    def cor_hex(self):
        return self.HEX.get(self.cores, '#1976f3')
    logista = models.ForeignKey(Logista, on_delete=models.CASCADE, blank=True, null=True) # ESTÁ COMO OPICIONAL PROVISÓRIAMENTE
