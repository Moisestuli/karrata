from django.conf.urls import url
from category.views import *

urlpatterns = (
    url(r'^$', categoria, name='categoria'),
)
