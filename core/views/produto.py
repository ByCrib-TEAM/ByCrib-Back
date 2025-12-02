from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action 
from core.models import Produto
from core.serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # Habilita busca por query param `?search=termo`
    filter_backends = [filters.SearchFilter]
    # Campos pesquisáveis: nome, descrição, nome da categoria e nome da marca
    search_fields = ['nome', 'descricao', 'categoria__nome', 'marca__nome']

    @action(detail=False, methods=['get'])
    def destaques(self, request):
        """Endpoint de busca: /api/produtos/search/?q=termo"""
        query = request.query_params.get('q', '')

        if not query or len(query) < 2:
            return Response([])
        
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(nome__icontains=query) [:10]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)