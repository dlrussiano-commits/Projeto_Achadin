from .models import Loja
from django import forms

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['nome', 'logo', 'banner','categoria', 'logista']

