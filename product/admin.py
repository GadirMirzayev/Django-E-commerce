from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import (
    Product,
    ProductImage,
    Feature,
    DataSheet,
    ProductCategory,
    Review,
    Size,
    Color,
)

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('title', 'product_rating', 'short_description', 'price', 'color', 'size', 'description',)
    search_fields = ('title', 'product_rating', 'short_description', 'price', 'color', 'size', 'description',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_filter = ('image',)
    search_fields = ('image',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_filter = ('feature',)
    search_fields = ('feature',)


@admin.register(DataSheet)
class DataSheetAdmin(admin.ModelAdmin):
    list_filter = ('data_sheet',)
    search_fields = ('data_sheet',)


class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('id','title',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register(ProductCategory, ProductCategoryAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('users_rating', 'text',)
    search_fields = ('users_rating', 'text',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)
