from rest_framework import serializers
from core.models import Categoria

# 1. Serializer Auxiliar (Para subcategorias, se houver)
class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'slug'] 

# 2. Serializer Principal de Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    # Isso permite que o JSON mostre as subcategorias aninhadas
    subcategorias = SubCategoriaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Categoria
        fields = "__all__"