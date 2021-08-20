from rest_framework import serializers
from checkout.models import BasketItem
from django.contrib.auth import get_user_model

User = get_user_model()

from accounts.serializers import UserSerializer
from product.api.serializers import ProductSerializer


class BasketItemSerializer(serializers.ModelSerializer):
    client = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = [
            'id',
            'product',
            'quantity',
            'client',
        ]



class BasketItemCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    product_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BasketItem
        fields = [
            'id',
            'product',
            'quantity',
            'client',
            'product_details',
        ]

    def validate(self, data):
        request = self.context.get('request')
        data['client'] = request.user
        attrs = super().validate(data)
        return attrs

    def get_product_details(self, obj):
        return ProductSerializer(obj.product).data 

