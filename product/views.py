from django.shortcuts import render,redirect
from django.contrib import messages
from product.models import *
from product.forms import *
from index.forms import SubscriberForm
from django.views.generic import (
    ListView, DetailView, TemplateView,
)
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

# Create your views here.

def customer_review(request):
    context = {
        "product": product,
    }
    return render(request, "customer-review.html",context)


def product_details(request, id):
    form = ReviewForm()
    form1 = SubscriberForm()
    product = Product.objects.get(id=id)
    parent_reviews = Review.objects.filter(parent_review__isnull=True)
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = User.objects.filter(is_superuser=True).first()
            review.save()
            messages.success(request, 'Serh bildirdiyiniz ucun tesekkur edirik!')
            return redirect('/')
    context = {
        "product": product,
        'form1': form1,
        'form': form,
        'parent_reviews': parent_reviews
    }
    return render(request, "product-details.html", context)


class ProductDetailView(FormMixin,DetailView):
    form_class = ReviewForm 
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'product'
    queryset = Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_reviews'] = Review.objects.filter(parent_review__isnull=True)
        for a in Review.objects.all() :
            context["rating"] = [i for i in range(a.users_rating)]
        return context

    def get_success_url(self):
        return reverse_lazy("product:product_detail", kwargs={"pk": self.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.product =self.object
        therate = form.instance.product.product_rating
        form.save()
        return super().form_valid(form)


# def shop(request):
#     form1 = SubscriberForm()
#     products = Product.objects.all()
#     categories = ProductCategory.objects.all()
#     context = {
#         "products": products,
#         "categories": categories,
#         'form1': form1
#     }
#     return render(request, "shop.html", context)


class ProductListView(TemplateView):
    template_name = 'shop.html'


# class ProductListView(ListView):
#     model = Product
#     template_name = 'shop.html'
#     context_object_name = 'products'
#     #queryset = Product.objects.filter(is_published=True)

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         tags = self.request.GET.get('tags')
#         queryset = queryset.filter(is_published=True)
#         if tags:
#             queryset = queryset.filter(tag__id=int(tags))
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = ProductCategory.objects.all()
#         context['product_image'] = ProductImage.objects.all().first()
#         return context
