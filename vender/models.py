from django.db import models
from produtos.models import Produto

# Create your models here.
class Vender(models.Model):

    nome_cliente    = models.CharField(max_length=255, unique=True)
    quantidade      = models.IntegerField(default=1)
    produto         = models.ForeignKey(Produto)
    ultimo_pagamento = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    troco     = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    total_comprado   = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    primeria_compra = models.DateTimeField(auto_now_add=True)
    ultima_compra   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return "%s comprou %s" % ( self.nome_cliente , self.produto.nome )

    def total_comprado(self):

        self.total_comprado = + self.ultimo_pagamento

        return self.total_comprado

    def ultimo_troco(self, pagamento):
        self.troco = pagamento - self.produto.preco
        return self.troco

