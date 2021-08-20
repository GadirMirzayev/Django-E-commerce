from modeltranslation.translator import translator, TranslationOptions
from product.models import ProductCategory

class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(ProductCategory, ProductCategoryTranslationOptions)