from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Fatura(models.Model):
    funcionario = models.ForeignKey(User, blank=True, null=True)
    cliente = models.CharField(max_length=255, blank=True, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.0)
    quantidade = models.IntegerField(default=1)
    valor_entregar = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.0)
    troco = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente
