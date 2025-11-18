from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import ItemCarrinho
from core.serializers import ItemCarrinhoSerializer

class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    serializer_class = ItemCarrinhoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ItemCarrinho.objects.filter(
            carrinho__usuario=self.request.user,
            carrinho__finalizado=False
        )