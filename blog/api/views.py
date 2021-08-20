from rest_framework.response import Response
from rest_framework import status
from blog.models import Blog, BlogComment
from blog.api.serializers import (
    BlogSerializer, BlogCreateSerializer,
    BlogCommentSerializer, BlogCommentCreateSerializer,

)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BlogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return BlogCreateSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return BlogCreateSerializer


class BlogCommentList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return BlogCommentCreateSerializer

    def post(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        blog = Blog.objects.filter(pk=blog_id).first()
        comment_data = request.data
        serializer = BlogCommentCreateSerializer(data=comment_data, context={'request': request})
        if serializer.is_valid():
            serializer.save(blog = blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return BlogCommentCreateSerializer
