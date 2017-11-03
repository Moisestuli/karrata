
from django.conf.urls import url
from carrinho.views import *

urlpatterns = [

    url(r'^add/$', carrinho_add, name='autenticar'),
    url(r'^carrinho/$', carrinho_add, name='autenticar'),
    url(r'^remover/(?P<product_id>\d+)/$', carrinho_remover ),
    url(r'^comprar/$', carrinho_comprar),
]
