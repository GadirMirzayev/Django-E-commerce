from rest_framework.response import Response
from rest_framework import status
from product.models import Product, ProductCategory
from product.api.serializers import ProductSerializer, ProductCreateSerializer, ProductCategorySerializer, ProductCategoryCreateSerializer
from rest_framework.decorators import api_view


@api_view(('GET', 'POST'))
def products(request):
    if request.method == 'POST':
        product_data = request.data
        serializer = ProductCreateSerializer(data=product_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    products = Product.objects.filter(is_published=True)
    serializer = ProductSerializer(products, many=True, context={'request': request})

    # serialized_recipe_list = [recipe.serialized_data for recipe in recipes]
    # json_data = {
    #     'recipes': serialized_recipe_list
    # }
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductCreateSerializer(product, data=request.data, partial=True,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('GET', 'POST'))
def product_categories(request):
    if request.method == 'POST':
        category_data = request.data
        serializer = ProductCategoryCreateSerializer(data=category_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    categories = ProductCategory.objects.all()
    serializer = ProductCategorySerializer(categories, many=True, context={'request': request})

    # serialized_recipe_list = [recipe.serialized_data for recipe in recipes]
    # json_data = {
    #     'recipes': serialized_recipe_list
    # }
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        category = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)