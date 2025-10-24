from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from core.serializers.user import UserSerializer

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Valida email+senha e retorna access, refresh e dados do usuário.
    """
    def validate(self, attrs):
        email = attrs.get('email') or attrs.get('username')
        password = attrs.get('password')

        if not email or not password:
            raise AuthenticationFailed('Email e senha são obrigatórios.')

        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if user is None:
            raise AuthenticationFailed('Credenciais inválidas.')

        data = super().validate({'username': user.email, 'password': password})
        data['user'] = UserSerializer(user, context=self.context).data
        return data