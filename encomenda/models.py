from django.db import models
from django.contrib.auth.models import User

class Encomenda(models.Model):
    nome = models.CharField(max_length=255)
    pass
