from django.urls import path
from blog.api.views import (
    BlogList, BlogDetail, 
    BlogCommentList, BlogCommentDetail, 

)


urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blogs_api'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blogs_detail_api'),
    path('blogs/<int:pk>/comments/', BlogCommentList.as_view(), name='blog_comments_api' ),
    path('blog-comments/<int:pk>/', BlogCommentDetail.as_view(), name='blog_comments_detail_api'),
]