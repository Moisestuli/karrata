
from django.conf.urls import url, include
from django.contrib import admin
from autenticacao.views import home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', home_page, name='autenticar'),
    url(r'^accounts/', include('autenticacao.urls')),
    url(r'^produto/', include('produtos.urls')),
    url(r'^carrinho/', include('carrinho.urls')),
    url(r'^admin/', include('administrador.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^fornecedor/', include('fornecedor.urls')),
    url(r'^relatorios/', include('relatorios.urls')),
    url(r'^encomendar/', include('encomenda.urls')),
    url(r'^clientes/', include('cliente.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
