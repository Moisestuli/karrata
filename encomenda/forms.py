from django import forms
from encomenda.models import Encomenda


class EncomendaForm(forms.ModelForm):
    class Meta:
        model = Encomenda
        fields = ('nome','categoria','descricao','cliente','funcionario', 'quantidade')
