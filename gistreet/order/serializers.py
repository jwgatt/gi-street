from .models import Order, OrderItem
from rest_framework import serializers
from product.serializer import ProductSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ("price", "quantity", "product")


class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'product', 'first_name', 'last_name', 'email', 'user', 'phone', 'created_at', 'order',
                  'address', 'postal_code', 'items', 'stripe_token', 'paid_amount']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("price", "quantity", "product")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, )

    class Meta:
        model = Order
        fields = ['id', 'product', 'first_name', 'last_name', 'email', 'user', 'phone', 'created_at', 'order',
                  'address', 'postal_code', 'items', 'stripe_token']

    # Overide create functionality

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data, )

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
