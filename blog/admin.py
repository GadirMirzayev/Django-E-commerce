from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from blog.models import (
    Blog,
    BlogCategory,
    BlogComment,
    BlogTag,
    )
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ('title', 'image', 'text', 'author',)
    search_fields = ('title', 'image', 'text', 'author',)


class BlogCategoryAdmin(TranslationAdmin):
    list_display = ('id','title',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register(BlogCategory, BlogCategoryAdmin)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_filter = ('user','text',)
    search_fields = ('user','text',)


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)