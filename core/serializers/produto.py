from rest_framework import serializers
from core.models import Produto
# Importa o serializer que criamos acima
from .categoria import CategoriaSerializer
from .marca import MarcaSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    # Traz os detalhes da categoria junto com o produto
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    
    class Meta:
        model = Produto
        # fields="__all__" já traz a imagem do Cloudinary corretamente como URL
        fields = "__all__"