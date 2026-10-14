from produto.models import Produto
from django import forms

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco','quantidade','foto', 'descricao', 'loja']