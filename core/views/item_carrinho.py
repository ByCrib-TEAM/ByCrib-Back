from rest_framework import viewsets
from core.models import ItemCarrinho
from core.serializers import ItemCarrinhoSerializer

class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    