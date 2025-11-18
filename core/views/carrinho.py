from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.models import Carrinho, ItemCarrinho, Produto
from core.serializers import CarrinhoSerializer, ItemCarrinhoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carrinho.objects.filter(usuario=self.request.user, finalizado=False)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_or_create_carrinho(self):
        carrinho, _ = Carrinho.objects.get_or_create(
            usuario=self.request.user,
            finalizado=False
        )
        return carrinho

    def list(self, request):
        carrinho = self.get_or_create_carrinho()
        serializer = self.get_serializer(carrinho)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], url_path='adicionar')
    def adicionar_item(self, request):
        carrinho = self.get_or_create_carrinho()
        produto_id = request.data.get('produto')
        quantidade_raw = request.data.get('quantidade', 1)

        try:
            quantidade = max(1, int(quantidade_raw))
        except ValueError:
            return Response(
                {'error': 'A quantidade deve ser um número inteiro.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not produto_id:
            return Response(
                {'error': 'O campo "produto" é obrigatório.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            produto = Produto.objects.get(id=produto_id)
        except Produto.DoesNotExist:
            return Response(
                {'error': 'Produto não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        item, criado = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            produto=produto
        )

        if not criado:
            item.quantidade += quantidade

        item.save()

        return Response(
            ItemCarrinhoSerializer(item).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['post'], url_path='remover')
    def remover_item(self, request):
        carrinho = self.get_or_create_carrinho()
        produto_id = request.data.get('produto')

        if not produto_id:
            return Response(
                {'error': 'O campo "produto" é obrigatório.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            item = ItemCarrinho.objects.get(carrinho=carrinho, produto_id=produto_id)
            item.delete()
        except ItemCarrinho.DoesNotExist:
            return Response(
                {'error': 'Item não encontrado no carrinho.'},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'], url_path='finalizar')
    def finalizar(self, request):
        try:
            carrinho = Carrinho.objects.get(usuario=request.user, finalizado=False)
        except Carrinho.DoesNotExist:
            return Response(
                {'error': 'Nenhum carrinho ativo encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if not carrinho.itens.exists():
            return Response(
                {'error': 'O carrinho está vazio.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        carrinho.finalizado = True
        carrinho.save()

        return Response(
            {'message': 'Compra finalizada com sucesso!'},
            status=status.HTTP_200_OK
        )