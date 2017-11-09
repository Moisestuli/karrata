from django.db import models


class Category(models.Model):

    nome       = models.CharField(max_length=50)
    #slug       = models.SlugField(max_length=50, unique=True )
    descricao  = models.TextField()
    upload     = models.FileField(default='default.jpg', upload_to='categoria/')
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nome
