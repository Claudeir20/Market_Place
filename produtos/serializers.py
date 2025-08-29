from rest_framework import serializers
from .models import Produto, Pedido, PedidoItem


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'descricao', 'categoria']


class PedidoItemSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    produto_preco = serializers.DecimalField(
        source='produto.preco',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = PedidoItem
        fields = ['pedido', 'produto_id', 'quantidade', 'produto_nome', 'produto_preco']


class PedidoSerializer(serializers.ModelSerializer):
    pedido_id = serializers.UUIDField(read_only=True)
    item = PedidoItemSerializer(many=True, read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['pedido_id', 'cliente', 'item', 'subtotal']

    def get_subtotal(self, obj):
        return sum([item.subtotal for item in obj.item.all()])

