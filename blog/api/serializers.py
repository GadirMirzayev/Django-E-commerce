from rest_framework import serializers
from blog.models import Blog, BlogComment, BlogCategory, BlogTag
from accounts.serializers import UserSerializer



class BlogTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [
            'id',
            'title'
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = UserSerializer()
    tag = BlogTagSerializer(many=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'text',
            'image',
            'category',
            'author',
            'tag',
            'comments',
            'created_at',
        ]

    def get_comments(self, obj):
        comments = obj.comments.filter(parent_comment__isnull=True)
        return BlogCommentSerializer(comments, many=True).data 


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'text',
            'image',
            'category',
            'author',
            'tag',
            'created_at',
        ]



class BlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    sub_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogComment
        fields = [
            'id',
            'text',
            'user',
            'sub_comments',
            'created_at',
        ]

    def get_sub_comments(self, obj):
        sub_comments = obj.sub_comments.all()
        return BlogCommentSerializer(sub_comments, many=True).data 



class BlogCommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogComment
        fields = [
            'id',
            'text',
            'user',
            'created_at',
        ]
