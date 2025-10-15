from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet, CategoriaViewSet, ProdutoViewSet, CarrinhoViewSet, ItemCarrinhoViewSet, MarcaViewSet
router = DefaultRouter()

carrinho_list = CarrinhoViewSet.as_view({'get': 'list'})
adicionar_item = CarrinhoViewSet.as_view({'post': 'create_item'})

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
    path('api/', include(router.urls)),
    path('api/carrinho/', carrinho_list, name='carrinho'),
    path('api/carrinho/adicionar/', adicionar_item, name='adicionar_item')
]