from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProdutoListAPIView,ProdutoCreateAPIView,ProdutoRetrieveUpdateDestroyAPIView,PedidoViewSet, PedidoItemViewSet


router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedidos')
router.register(r'pedidos-item', PedidoItemViewSet, basename='pedidos-itens')


urlpatterns = [
    path('produtos/lista',ProdutoListAPIView.as_view(), name='produto-lista' ),
    path('produto/', ProdutoCreateAPIView.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProdutoRetrieveUpdateDestroyAPIView.as_view(), name='produtos-detail'),
    
]

urlpatterns += router.urls