import token
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet, CategoriaViewSet, ProdutoViewSet, CarrinhoViewSet, ItemCarrinhoViewSet, MarcaViewSet
router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'produtos', ProdutoViewSet, basename='produtos')
router.register(r'carrinhos', CarrinhoViewSet, basename='carrinhos')
router.register(r'itens-carrinho', ItemCarrinhoViewSet, basename='itens-carrinho')
router.register(r'marcas', MarcaViewSet, basename='marcas')


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)
    ),
    #JWT
     path(
         'api/token/',
           TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
          TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/verify/',
          TokenVerifyView.as_view(), name='token_verify'
    ),


    


]