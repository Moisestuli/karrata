from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from produtos.models import Produto
from category.models import Category

class Encomenda(models.Model):

    nome = models.ForeignKey(Produto)
    categoria = models.ForeignKey(Category, default=1)
    descricao = models.TextField(blank=True)
    cliente = models.ManyToManyField(Cliente)
    funcionario = models.ForeignKey(User)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return "encomenda: {} | Quantidade {}".format(self.nome, self.quantidade)
