from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=9, blank=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    actualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
