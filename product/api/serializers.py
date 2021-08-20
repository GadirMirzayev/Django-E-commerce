from rest_framework import serializers
from product.models import Product, ProductCategory, ProductImage, Size, Color


class SizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Size
        fields = [
            'id',
            'title',
        ]



class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = [
            'id',
            'title',
        ]



class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    category = serializers.CharField(source='category.title')
    size = SizeSerializer(many=True)
    color = ColorSerializer(many=True)
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'product_rating',
            'short_description',
            'slug',
            'price',
            'image',
            'discount',
            'description',
            'color',
            'size',
            'category',
            'set_discount_price',
            'get_absolute_url',
        ]

    def get_image(self, obj):
        image = obj.product_image.filter(is_published=True).first()
        return ProductImageSerializer(image).data 



class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'product_rating',
            'short_description',
            'slug',
            'price',
            'discount',
            'description',
            'color',
            'size',
            'category',
            'set_discount_price',
        ]



class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.id')

    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
            'product',
        ]



class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
        ]



class ProductCategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
        ]