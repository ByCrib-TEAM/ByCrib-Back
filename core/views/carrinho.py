from rest_framework.viewsets import ModelViewSet
from core.models import Carrinho
from core.serializers import CarrinhoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer