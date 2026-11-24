from .models import Loja
from django import forms

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['nome', 'logo', 'banner', 'categoria', 'cores',
                  'estilo_botao', 'texto_banner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cores'].initial = 'b'