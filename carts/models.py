from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Cart(models.Model):

    produto          = models.CharField(max_length=255)
    cliente          = models.CharField(max_length=255)
    quantidade       = models.IntegerField(default=1)
    preco         = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    funcionario      = models.CharField(max_length=255,default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cliente: {} | Produto: {}".format(self.cliente, self.produto)
