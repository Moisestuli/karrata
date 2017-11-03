from django import forms
from django.contrib.auth.forms import UserCreationForm
from fornecedor.models import Fornecedor


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('nome','telefone','cidade')

