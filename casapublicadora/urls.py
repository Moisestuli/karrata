
from django.conf.urls import url, include
from django.contrib import admin
from autenticacao.views import home_page

urlpatterns = [

    url(r'^$', home_page, name='autenticar'),
    url(r'^accounts/', include('autenticacao.urls')),
    url(r'^produto/', include('produtos.urls')),
    url(r'^carrinho/', include('carrinho.urls')),
    url(r'^admin/', include('administrador.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^fornecedor/', include('fornecedor.urls')),
]
