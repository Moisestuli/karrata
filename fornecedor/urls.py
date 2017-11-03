from django.conf.urls import url
from fornecedor.views import *


urlpatterns = [

    #url(r'^eliminar/$', fornecedor_eliminar, name='eliminar'),
    url(r'^eliminar/(?P<username>[-\w]+)/$', fornecedor_eliminar ),
    url(r'^editar/(?P<username>[-\w]+)/$', fornecedor_editar ),
    url(r'^actualizar/(?P<username>[-\w]+)/$', fornecedor_actualizar ),
]
