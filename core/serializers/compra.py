from rest_framework import serializers
from core.models import Compra, Carrinho, ItemCarrinho
from core.serializers.carrinho import ItemCarrinhoSerializer

class CompraSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.email', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    itens = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = Compra
        fields = ['id', 'usuario', 'carrinho', 'status', 'itens', 'total', 'criado_em', 'atualizado_em']
        read_only_fields = ['usuario', 'status', 'itens', 'total', 'criado_em', 'atualizado_em']
    
    def get_itens(self, obj):
        return ItemCarrinhoSerializer(obj.carrinho.itens.all(), many=True).data
    
    def get_total(self, obj):
        return sum(item.quantidade * item.produto.preco for item in obj.carrinho.itens.all())
