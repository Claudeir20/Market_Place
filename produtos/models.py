from django.db import models
from django.conf import settings
import uuid

# Create your models here.


class Produto(models.Model):
    class CategoriaCHoiche(models.TextChoices):
        ELETRONICO = 'Eletronico'
        LIMPEZA = 'Limpeza'
        CASA = 'Casa'
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(
        max_length=10,
        choices= CategoriaCHoiche.choices
    )

    @property
    
    def tem_estoque(self):
        return self.estoque > 0
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    pedido_id = models.UUIDField(primary_key= True, default=uuid.uuid4)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ManyToManyField(Produto, through="PedidoItem", related_name='pedidos')

    
    def __str__(self):
        return f"Pedido: {self.pedido_id}"

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='item')
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    @property
    def subtotal(self):
        return self.produto_id.preco * self.quantidade

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} no pedido {self.pedido.pedido_id}'