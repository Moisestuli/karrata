from django.conf.urls import url
from administrador.views import *
from funcionario.views import *
from fornecedor.views import *

urlpatterns = [

    url(r'^criar-funcionario/$', criafuncionario, name='criafuncionario'),
    url(r'^fornecedor/$', adiciona_fornecedor, name="fornecedor"),
    url(r'^configuracao/funcionario/(?P<pk>[0-9]+)/$', funcionario_editar),
    url(r'^configuracao/fornecedor/(?P<pk>[0-9]+)/$', fornecedor_editar),
    url(r'^analise/$', analise_dados, name='analise'),
    url(r'^eliminar/(?P<username>[-\w]+)/$', funcionario_eliminar ),
    url(r'^editar/(?P<username>[-\w]+)/$', funcionario_editar ),
]
