from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Autenticação JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Documentação (Swagger/Redoc)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# Importação das Views (Certifique-se que todas existem em core/views.py)
from core.views import (
    UserViewSet,
    CategoriaViewSet,
    ProdutoViewSet, # ✅ Essencial para o filtro funcionar
    CarrinhoViewSet,
    ItemCarrinhoViewSet,
    MarcaViewSet,
    CompraViewSet,
)

# Configuração das Rotas da API
router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'produtos', ProdutoViewSet, basename='produtos') # Endpoint: /api/produtos/
router.register(r'carrinhos', CarrinhoViewSet, basename='carrinhos')
router.register(r'itens-carrinho', ItemCarrinhoViewSet, basename='itens-carrinho')
router.register(r'marcas', MarcaViewSet, basename='marcas')
router.register(r'compras', CompraViewSet, basename='compras')

urlpatterns = [
    # Painel Administrativo do Django
    path('admin/', admin.site.urls),

    # ---------------------------------------------------------
    # Documentação da API (Muito útil para ver os filtros)
    # Acesso: http://localhost:8000/api/swagger/
    # ---------------------------------------------------------
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # ---------------------------------------------------------
    # Rotas Principais (Inclui todas as registradas no router)
    # ---------------------------------------------------------
    path('api/', include(router.urls)),

    # ---------------------------------------------------------
    # Autenticação (Login e Tokens)
    # ---------------------------------------------------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# ---------------------------------------------------------
# Configuração para Servir Imagens (Arquivos de Mídia)
# ISSO É CRUCIAL PARA AS FOTOS DOS PRODUTOS APARECEREM
# ---------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)