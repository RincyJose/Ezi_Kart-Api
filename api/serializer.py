from rest_framework import serializers
from .models import Order,Order_item,User


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user_data = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


        

class UserSerializer(serializers.ModelSerializer):
    order_list_data = OrderSerializer(many=True)
        
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_order = validated_data.pop('order_list_data')
        user_instance = User.objects.create(**validated_data)
        print(user_instance)
        
        for list in user_order:
            list_data = list.pop('user_data')
            request_order = Order.objects.create(id=user_instance,**list)
            
            for order_item_data in list_data:
                Order_item.objects.create(id=request_order,**order_item_data)                                                              
        
        return user_instance