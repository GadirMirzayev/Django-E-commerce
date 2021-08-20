from modeltranslation.translator import translator, TranslationOptions
from blog.models import BlogCategory

class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(BlogCategory, BlogCategoryTranslationOptions)