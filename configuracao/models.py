from django.db import models
from django.contrib.auth.models import User

class Configuracao(models.Model):
    """docstring for Configuracao."""
    perfil = models.OneToOneField(User, null=True)
    imagem = models.FileField(default='profile/default.jpg', upload_to='profile/')
    telefone = models.CharField(max_length=9, blank=True)
    email    = models.EmailField(null=True)
    cidade   = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "%s " % self.perfil
