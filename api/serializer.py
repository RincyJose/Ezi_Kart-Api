from rest_framework import serializers
from .models import Order,Order_item

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_item
        fields = '__all__'
        

class OrderSerializer(serializers.ModelSerializer):
    user_orders = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user_order = validated_data.pop('user_orders')
        order_instance = Order.objects.create(**validated_data)
        for hobby in user_order:
            Order_item.objects.create(user=order_instance,**hobby)
        return order_instance