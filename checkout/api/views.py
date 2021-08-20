from rest_framework.response import Response
from rest_framework import status
from checkout.models import BasketItem
from checkout.api.serializers import (
    BasketItemSerializer, BasketItemCreateSerializer
)

from rest_framework.views import APIView
from product.models import Product



class BasketItemListView(APIView):
    def get(self, request,*args,**kwargs):
        basket_items = BasketItem.objects.all()
        serializer = BasketItemSerializer(basket_items, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request,*args,**kwargs):
        basket_data = request.data
        serializer = BasketItemCreateSerializer(data=basket_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        product_id = basket_data['product']
        product = Product.objects.filter(id=product_id).first()
        basket = BasketItem.objects.filter(product=product, client=request.user).first()
        
        if basket:
            # basket.quantity += 1
            basket.save()
        else :
            serializer.save(product=product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BasketItemDetailView(APIView):
    def get(self, request, *args, **kwargs):
        basket_item_id = kwargs.get('pk')
        basket_item = BasketItem.objects.filter(pk=basket_item_id).first()
        serializer = BasketItemSerializer(basket_item, context={'request': request},)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        basket_item_id = kwargs.get('pk')
        basket_item = BasketItem.objects.filter(pk=basket_item_id).first()
        serializer = BasketItemCreateSerializer(data=request.data, instance=basket_item, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        basket_item_id = kwargs.get('pk')
        basket_item = BasketItem.objects.filter(pk=basket_item_id)
        basket_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)