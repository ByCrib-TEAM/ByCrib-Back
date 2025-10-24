from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from core.serializers.authentication import EmailTokenObtainPairSerializer

class EmailTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = EmailTokenObtainPairSerializer