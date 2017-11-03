from django.db import models

# Create your models here.
class Fornecedor(models.Model):

    nome       = models.CharField(max_length=255, unique=True)
    telefone   = models.CharField(max_length=100, unique=True)
    cidade     = models.CharField(max_length=255)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
