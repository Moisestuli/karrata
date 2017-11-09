from django.conf.urls import url
from carts.views import adiciona_carrinho, mostra_carrinho, processa_carrinho
urlpatterns = [
    url(r'^adiciona/(?P<pk>[0-9]+)/$', adiciona_carrinho, name='carrinho'),
    url(r'^processa/$', processa_carrinho, name='processa-carrinho'),
    url(r'^ver/$', mostra_carrinho, name='mostra-carrinho'),
]
