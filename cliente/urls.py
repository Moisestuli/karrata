from django.conf.urls import url
from cliente.views import clientes

urlpatterns = (
    url(r'^$', clientes, name='clientes'),
)
