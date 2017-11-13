from django import froms
from Configuracao.models import Perfil
class PerfilForm(forms.FormModel):
    model = Perfil
    fields = ('perfil','imagem')
