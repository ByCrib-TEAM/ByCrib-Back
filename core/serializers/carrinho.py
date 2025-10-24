from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Carrinho, ItemCarrinho, Produto
from core.serializers.produto import ProdutoSerializer

class ItemCarrinhoSerializer(ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), source='produto', write_only=True
    )
    produto_nome = serializers.ReadOnlyField(source='produto.nome')
    preco_unitario = serializers.ReadOnlyField(source='produto.preco')
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = ['id', 'produto', 'produto_nome', 'quantidade', 'preco_unitario', 'subtotal']

    def get_subtotal(self, obj):
        return obj.quantidade * obj.produto.preco
    

class CarrinhoSerializer(ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'criado_em', 'atualizado_em', 'finalizado', 'itens', 'total']
        read_only_fields = ['usuario', 'criado_em', 'atualizado_em']

    def get_total(self, obj):
        return sum(item.quantidade * item.produto.preco for item in obj.itens.all())