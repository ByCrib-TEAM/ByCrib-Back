from django.db import models
from .categoria import Categoria
from .marca import Marca
from cloudinary.models import CloudinaryField

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

    imagem = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]
