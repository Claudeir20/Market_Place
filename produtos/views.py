from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from .serializers import PedidoItemSerializer, ProdutoSerializer, PedidoSerializer
from .models import Pedido, PedidoItem, Produto
from .permissions import IsAdmin, IsCliente, IsVendedor, IsAdminOrVendedor
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ProdutoCreateAPIView(CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsVendedor]
    
class ProdutoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsVendedor]


class ProdutoListAPIView(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]



class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(cliente=self.request.user)



class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer
    permission_classes = [IsAuthenticated]