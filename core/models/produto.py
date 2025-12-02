from django.db import models
from django.utils.text import slugify # Necessário para criar o slug automaticamente
from cloudinary.models import CloudinaryField

# Importações dos outros models
from .categoria import Categoria
from .marca import Marca

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    
    # ADICIONADO: Slug é essencial para o Frontend acessar /produtos/nome-do-produto
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT, # PROTECT é ótimo, evita deletar categoria com produtos
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

    # Lógica para gerar o slug automaticamente ao salvar
    def save(self, *args, **kwargs):
        if not self.slug and self.nome:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]