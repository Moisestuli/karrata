from django.db import models
from produtos.models import Produto


# Create your models here.
class Venda(models.Model):

    nome_client      = models.CharField(max_length=255, unique=True)
    telefone         = models.CharField(max_length=255, blank=True)
    cidade           = models.CharField(max_length=255)
    email            = models.EmailField(blank=True)
    no_compras       = models.IntegerField(default=1)
    preco            = models.DateTimeField(default=0.0)
    deu              = models.DateTimeField(default=0.0)
    ult_troco        = models.DateTimeField(default=0.0,blank=True)
    ult_valor        = models.DateTimeField(default=0.0,blank=True)
    ult_compra       = models.DateTimeField(default=0.0, blank=True)
    total_compra     = models.DateTimeField(default=0.0, blank=True)
    total_troco      = models.DateTimeField(default=0.0, blank=True)
    total_valor      = models.FloatField(default=0.0, blank=True)
    produto          = models.ForeignKey(Produto)
    prim_dia_compra  = models.DateTimeField(auto_now_add=True)
    ult_dia_compra   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return "Cliente: %s  " % self.nome_client

    def total_compra(self, quatidade ):

        return quatidade * self.produto.preco.replace(',','.')






