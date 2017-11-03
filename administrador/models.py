from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Administrador(models.Model):

    nome = models.OneToOneField(User)
    nascimento = models.DateField(auto_now_add=False)
    cidade     = models.CharField(max_length=255)
    telefone   = models.IntegerField(default=0)

    def __str__(self):
        return self.nome



