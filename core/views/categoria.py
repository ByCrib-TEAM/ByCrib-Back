from rest_framework.viewsets import ModelViewSet
# Importe também o Produto e o ProdutoSerializer
from core.models import Categoria, Produto
from core.serializers import CategoriaSerializer, ProdutoSerializer

# 1. Seu código original (Mantido)
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# 2. O código novo necessário para o Filtro funcionar
class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    
    def get_queryset(self):
        """
        Sobrescreve a busca padrão para permitir filtrar pela URL.
        Exemplo: /api/produtos/?categoria=2 (Onde 2 é o ID da categoria)
        """
        # Começa pegando todos os produtos
        queryset = Produto.objects.all().order_by('id')
        
        # Pega o parâmetro 'categoria' da URL (se existir)
        categoria_id = self.request.query_params.get('categoria', None)

        if categoria_id is not None:
            # Lógica de Filtro:
            # Filtra produtos onde o campo 'categoria' (ID) é igual ao parâmetro recebido
            queryset = queryset.filter(categoria__id=categoria_id)
            
            # DICA PRO: Se quiser que ao clicar na categoria PAI (ex: Roupas)
            # traga também as filhas (ex: Camisetas), a lógica muda um pouco.
            # Se precisar disso, me avise! Por enquanto, filtro exato é mais simples.

        return queryset