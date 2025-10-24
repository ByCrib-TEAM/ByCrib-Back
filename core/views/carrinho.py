from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.models import Carrinho, ItemCarrinho, Produto
from core.serializers import CarrinhoSerializer, ItemCarrinhoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    # Gerencia o carrinho de compras do usuário autenticado
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    # Queryset e criação
    def get_queryset(self):
        # Retorna apenas o carrinho do usuário logado
        return Carrinho.objects.filter(usuario=self.request.user, finalizado=False)

    def perform_create(self, serializer):
        # Associa o carrinho ao usuário logado
        serializer.save(usuario=self.request.user)

    def get_or_create_carrinho(self):
        # Obtém ou cria um carrinho ativo
        carrinho, _ = Carrinho.objects.get_or_create(usuario=self.request.user, finalizado=False)
        return carrinho

    def list(self, request):
        carrinho = self.get_or_create_carrinho()
        serializer = self.get_serializer(carrinho)
        return Response(serializer.data)

    # Ações personalizadas
    @action(detail=False, methods=['post'], url_path='adicionar')
    def adicionar_item(self, request):
        # Adiciona um produto ao carrinho
        carrinho = self.get_or_create_carrinho()
        produto_id = request.data.get('produto')
        quantidade = int(request.data.get('quantidade', 1))

        if not produto_id:
            return Response({'error': 'O campo "produto" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            produto = Produto.objects.get(id=produto_id)
        except Produto.DoesNotExist:
            return Response({'error': 'Produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        if not criado:
            item.quantidade += quantidade
        item.save()

        return Response(ItemCarrinhoSerializer(item).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='remover')
    def remover_item(self, request):
        # Remove um item do carrinho
        carrinho = self.get_or_create_carrinho()
        produto_id = request.data.get('produto')

        if not produto_id:
            return Response({'error': 'O campo "produto" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = ItemCarrinho.objects.get(carrinho=carrinho, produto_id=produto_id)
            item.delete()
        except ItemCarrinho.DoesNotExist:
            return Response({'error': 'Item não encontrado no carrinho.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Item removido com sucesso.'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'], url_path='finalizar')
    def finalizar(self, request):
        # Finaliza o carrinho e impede novas alterações
        try:
            carrinho = Carrinho.objects.get(usuario=request.user, finalizado=False)
        except Carrinho.DoesNotExist:
            return Response({'error': 'Nenhum carrinho ativo encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        carrinho.finalizado = True
        carrinho.save()

        return Response({'message': 'Compra finalizada com sucesso!'}, status=status.HTTP_200_OK)