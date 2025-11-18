from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserWriteSerializer, UserReadSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserWriteSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        if self.action == 'me':
            return [IsAuthenticated()]
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Operação não permitida."},
            status=status.HTTP_403_FORBIDDEN
        )

    def retrieve(self, request, *args, **kwargs):
        return Response(
            {"detail": "Operação não permitida."},
            status=status.HTTP_403_FORBIDDEN
        )

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        """Consultar ou editar o próprio usuário"""
        user = request.user

        if request.method == 'GET':
            return Response(UserReadSerializer(user).data)

        serializer = UserWriteSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(UserReadSerializer(user).data)