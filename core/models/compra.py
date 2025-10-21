from django.db import models
from django.conf import settings
from core.models.carrinho import Carrinho

class Compra(models.Model):
    class StatusCompra(models.TextChoices):
        CARRINHO = 'CARRINHO', 'Carrinho'
        REALIZADO = 'REALIZADO', 'Realizado'
        PAGO = 'PAGO', 'Pago'
        ENTREGUE = 'ENTREGUE', 'Entregue'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='compras'
    )

    carrinho = models.OneToOneField(
        Carrinho,
        on_delete=models.CASCADE,
        related_name='compra'
    )

    status = models.CharField(
        max_length=20,
        choices=StatusCompra.choices,
        default=StatusCompra.CARRINHO
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Compra #{self.id} - Usuário: {self.usuario} - {self.status}'
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-criado_em']