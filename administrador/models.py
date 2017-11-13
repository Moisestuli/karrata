from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Administrador(models.Model):

    nome = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.nome
