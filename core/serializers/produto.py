from rest_framework import serializers
from core.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    marca = serializers.StringRelatedField()
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'estoque',
            'categoria',
            'marca',
            'imagem_url',
        ]

    def get_imagem_url(self, obj):
        if obj.imagem:
            return obj.imagem.url
        return None
