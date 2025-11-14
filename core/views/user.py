from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserWriteSerializer, UserReadSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    # Serializer padrão para criação/atualização
    serializer_class = UserWriteSerializer

    def get_serializer_class(self):
        """Usa UserReadSerializer para list e retrieve, Write para create/update"""
        if self.action in ['list', 'retrieve', 'me']:
            return UserReadSerializer
        return UserWriteSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Return the current authenticated user"""
        serializer = UserReadSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    