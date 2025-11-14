from rest_framework import serializers
from core.models import ItemCarrinho, Produto

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    produto_id = serializers.PrimaryKeyRelatedField(
        source='produto', queryset=Produto.objects.all()
    )

    class Meta:
        model = ItemCarrinho
        fields = ['id', 'carrinho', 'produto_id', 'quantidade']

    def get_subtotal(self, obj):
        return obj.quantidade * obj.produto.preco