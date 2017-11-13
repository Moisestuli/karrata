from django.conf.urls import url
from carts.views import *
urlpatterns = [
    url(r'^adiciona/(?P<pk>[0-9]+)/$', adiciona_carrinho, name='carrinho'),
    url(r'^processa/$', processa_carrinho, name='processa-carrinho'),
    url(r'^ver/$', mostra_carrinho, name='mostra-carrinho'),
    url(r'^futura/$', futurar_agora, name='futurar'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', eliminar_carrinho, name = 'eliminar'),
]
