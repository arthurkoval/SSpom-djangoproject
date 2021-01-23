from rest_framework import serializers
from .models import CustomUser
from order.models import Order

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


