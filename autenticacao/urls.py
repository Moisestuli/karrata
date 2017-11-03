from django.conf.urls import url
from autenticacao.views import logar, logout

urlpatterns = [

    url(r'^logar/$', logar, name='logar'),
    url(r'^logout/$', logout, name='logout'),
]
