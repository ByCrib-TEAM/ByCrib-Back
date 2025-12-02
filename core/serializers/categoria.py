from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Categoria, Produto

# 1. Serializer Auxiliar (Para as subcategorias aparecerem com ID e Nome)
class SubCategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        # Se você adicionou o campo 'slug' no model, adicione aqui: ['id', 'nome', 'slug']
        fields = ['id', 'nome'] 

# 2. Serializer Principal de Categoria (O que você enviou, atualizado)
class CategoriaSerializer(ModelSerializer):
    # Aqui substituímos o StringRelatedField pelo serializer acima.
    # Isso faz o JSON virar [{"id": 2, "nome": "Bermudas"}] em vez de ["Bermudas"]
    subcategorias = SubCategoriaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Categoria
        fields = "__all__"

# 3. Serializer de Produto (Necessário para a listagem no Vue)
class ProdutoSerializer(ModelSerializer):
    # Traz os detalhes da categoria junto com o produto
    categoria = CategoriaSerializer(read_only=True)
    
    # Campo extra para garantir a URL completa da imagem (boa prática)
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = "__all__"

    def get_imagem_url(self, obj):
        # Retorna a URL completa (http://localhost...) para o Vue não ter erro de imagem quebrada
        request = self.context.get('request')
        if obj.imagem and request:
            return request.build_absolute_uri(obj.imagem.url)
        return None