# loja/models/produto.py
from django.db import models
from uploader.models import Image
from .categoria import Categoria
from .marca import Marca

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="produtos"
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.SET_NULL,
        related_name="produtos",
        null=True,
        blank=True
    )
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]