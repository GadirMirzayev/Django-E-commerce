from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import *
from blog.forms import *
from index.forms import SubscriberForm
from django.views.generic import (
    ListView, DetailView
)
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


# Create your views here.

# def blog(request):
#     form1 = SubscriberForm()
#     blogs = Blog.objects.all()
#     context = {
#         "blogs": blogs,
#         'form1': form1
#     }
#     return render(request, "blog.html", context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 1
    context_object_name = 'blogs'
    #queryset = Blog.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tag__id=int(tags))
        return queryset


# def blog_details(request,id):
#     form = CommentForm()
#     form1 = SubscriberForm()
#     blog = Blog.objects.get(id=id)
#     blog_categories = BlogCategory.objects.all()
#     blog_tags = BlogTag.objects.all()
#     parent_comments = BlogComment.objects.filter(parent_comment__isnull=True)
#     latest_posts = Blog.objects.order_by('-created_at')[:3]
#     if request.method == 'POST':
#         form = CommentForm(data=request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = blog
#             comment.user = User.objects.filter(is_superuser=True).first()
#             comment.save()
#             messages.success(request, 'Serh bildirdiyiniz ucun tesekkur edirik!')
#             return redirect('/')
#     context = {
#         "blog": blog,
#         "blog_categories": blog_categories,
#         "latest_posts": latest_posts,
#         "blog_tags": blog_tags,
#         'form1': form1,
#         'form': form,
#         'parent_comments': parent_comments
#     }
#     return render(request, "blog-details.html",context)

class BlogDetailView(FormMixin,DetailView):
    form_class = CommentForm 
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    queryset = Blog.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_categories'] = BlogCategory.objects.all() 
        context['blog_tags'] = BlogTag.objects.all()
        context['parent_comments'] = BlogComment.objects.filter(parent_comment__isnull=True)
        context['latest_posts'] = Blog.objects.order_by('-created_at')[:3]
        return context


    def get_success_url(self):
        return reverse_lazy("blog:blogdetail", kwargs={"pk": self.object.id})


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.blog = self.object
        form.save()
        return super().form_valid(form)

