from django.db import models
from category.models import Category
from fornecedor.models import Fornecedor

# Create your models here.
class Produto(models.Model):

    nome          = models.CharField(max_length=255, unique=True)
    slug          = models.SlugField(max_length=255,default='', blank=True)
    sku           = models.CharField(max_length=50, blank=True)
    upload        = models.FileField(default="produtos/default.jpg", upload_to='produtos/')
    preco         = models.DecimalField(max_digits=9, decimal_places=2)
    old_preco     = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.0)
    is_active     = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    quantity      = models.IntegerField(default=1)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    categories    = models.ManyToManyField(Category)
    fornecedores  = models.ManyToManyField(Fornecedor)


    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
