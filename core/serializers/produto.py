from rest_framework import serializers
from core.models import Produto, Categoria, Marca # Certifique-se de importar Categoria e Marca

# 1. Serializer Auxiliar para Categoria
# Isso garante que o Vue receba { id: 5, nome: "Bermudas" } e não apenas "Bermudas"
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'slug'] # Slug é opcional, mas ID e Nome são essenciais

# 2. Serializer Auxiliar para Marca
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nome']

# 3. Serializer Principal do Produto
class ProdutoSerializer(serializers.ModelSerializer):
    # Substituímos StringRelatedField pelos serializers acima
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    
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

    # BLINDAGEM CONTRA ERRO 500
    def get_imagem_url(self, obj):
        try:
            if obj.imagem:
                # Retorna a URL segura do Cloudinary
                return obj.imagem.url
        except Exception as e:
            # Se der erro (ex: falta configuração no Render),
            # ele imprime o erro no log do Render mas NÃO DERRUBA O SITE.
            print(f"⚠️ Erro ao gerar imagem para o produto {obj.id}: {e}")
            return None
        return None