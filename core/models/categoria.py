from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    # Adicionado SLUG para funcionar nas URLs do Vue (ex: /produtos/bermudas)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    # Seu campo de subcategorias (hierarquia)
    pai = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategorias",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        # Gera o slug automaticamente se não existir
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

 