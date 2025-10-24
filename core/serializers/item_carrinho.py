from rest_framework import serializers
from core.models import ItemCarrinho

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = "__all__"