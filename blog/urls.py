from django.urls import path, re_path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name="blog"),
    path('blog-details/<int:pk>/', BlogDetailView.as_view(), name="blogdetail"),
]