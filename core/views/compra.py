from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Compra, Carrinho
from core.serializers import CompraSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Compra.objects.filter(usuario=self.request.user)
            .select_related('carrinho', 'usuario')
        )

    def perform_create(self, serializer):
        carrinho = Carrinho.objects.filter(usuario=self.request.user, finalizado=False).first()
        if not carrinho:
            raise serializers.ValidationError('Nenhum carrinho ativo encontrado.')

        serializer.save(usuario=self.request.user, carrinho=carrinho)

    @action(detail=True, methods=['post'])
    def finalizar(self, request, pk=None):
        compra = self.get_object()

        if compra.status != Compra.StatusCompra.CARRINHO:
            return Response(
                {'error': 'Esta compra já foi finalizada ou processada.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            compra.finalizar_compra()
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'Compra finalizada com sucesso!',
            'nova_situacao': compra.get_status_display()
        }, status=status.HTTP_200_OK)