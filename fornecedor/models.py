from django.db import models

# Create your models here.
class Fornecedor(models.Model):

    nome = models.CharField(max_length=255, unique=True)
    telefone = models.CharField(max_length=100,blank=True, unique=True)
    cidade = models.CharField(max_length=255, blank=True)
    img = models.FileField(default="profile/default.jpg", upload_to="profile/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
