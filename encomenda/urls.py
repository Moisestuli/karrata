from django.conf.urls import url
from category.models import Category
from encomenda.views import *

urlpatterns = (
    url(r'^$', encomendar, name='encomendar'),
)
