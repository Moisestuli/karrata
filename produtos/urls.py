from django.conf.urls import url
from produtos.views import *
from vender.views import *

urlpatterns = [

    url(r'^todos/$', todos_produtos, name='todos'),
    url(r'^vender/(?P<produto_slug>[-\w]+)/$', vender_produto, name='vender'),
    url(r'^adiciona/(?P<produto_slug>[-\w]+)/$', produto_adiciona),
    url(r'^single/(?P<pk>[-\w]+)/$', produto_single ),

]
