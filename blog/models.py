from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField('Title', max_length=127)

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    title = models.CharField('Title', max_length=127)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField('Image', upload_to='blog_images',null=True, blank=True)
    title = models.CharField('Title', max_length=127)
    text = models.TextField('Context',)
    is_published = models.BooleanField('Is Published', default=True)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, db_index=True, blank=True, null=True,
                               related_name='blog',)
    category = models.ForeignKey(BlogCategory, verbose_name='Blog Category',
                                    on_delete=models.CASCADE, db_index=True, blank=True, related_name='blog')
    tag = models.ManyToManyField(BlogTag, verbose_name='Blog Tag', db_index=True, blank=True,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    text = models.TextField('Context',)
    user = models.ForeignKey(User, verbose_name='Author name', on_delete=models.CASCADE, db_index=True,
                               related_name='comment',)
    blog = models.ForeignKey(Blog, verbose_name='Blog',
                                    on_delete=models.CASCADE, db_index=True, related_name='comments')
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True, related_name='sub_comments', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text