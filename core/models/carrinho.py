from django.db import models
from django.conf import settings

class Carrinho(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="carrinhos"
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Carrinho #{self.id} - Usuário: {self.usuario}"
    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"
        ordering = ["-criado_em"]