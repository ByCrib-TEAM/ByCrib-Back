from rest_framework.viewsets import ModelViewSet
from core.models import ItemCarrinho
from core.serializers import ItemCarrinhoSerializer

class ItemCarrinhoViewSet(ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
