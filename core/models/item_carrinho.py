from django.db import models
from core.models import Carrinho, Produto

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name='itens'
    )
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='itens_carrinho'
    )
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} (Carrinho #{self.carrinho.id})'
    
    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        ordering = ['carrinho', 'produto']
        unique_together = ('carrinho', 'produto')