from django.db import models
from .categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")

    def __str__(self):
        return self.nome
