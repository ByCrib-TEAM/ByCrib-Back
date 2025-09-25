from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    subcategorias = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Categoria
        fields = "__all__"