from django.conf.urls import url
from relatorios.views import *

urlpatterns = (
    url(r'^$', relatorios, name='relatorios'),
)
