from django import forms
from produtos.models import Produto


class ProdutoAdminForm(forms.ModelForm):
    class Meta:
        model = Produto
        file_now = forms.FileField()
        fields = ('nome','preco','upload','categories', 'fornecedores')
