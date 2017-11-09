from django import forms
from  category.models import Category


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('nome','descricao','upload')
