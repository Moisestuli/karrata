from django import forms
from vendas.models import Venda
class VendaAdminForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ('nome_client','telefone','cidade','email','produto','deu',)