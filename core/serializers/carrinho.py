from rest_framework.serializers import ModelSerializer
from core.models import Carrinho, ItemCarrinho
from core.serializers.produto import ProdutoSerializer

class ItemCarrinhoSerializer(ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = ItemCarrinho
        fields = ['id', 'produto', 'quantidade']

class CarrinhoSerializer(ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'criado_em', 'atualizado_em', 'finalizado', 'itens']
