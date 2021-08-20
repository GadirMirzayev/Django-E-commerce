from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from slugify import slugify
import datetime

User = get_user_model()

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField('Title', max_length=127)

    def __str__(self):
        return self.title



class Size(models.Model):
    title = models.CharField("Title", max_length=7)

    def __str__(self):
        return self.title



class Color(models.Model):
    title = models.CharField('Title', max_length=31)

    def __str__(self):
        return self.title

    

class Product(models.Model):
    title = models.CharField('Title', max_length=127)
    product_rating = models.DecimalField('Product Rating', max_digits=3, decimal_places=2)
    short_description = models.CharField('Short Description', max_length=255)
    slug = models.SlugField('Slug', default='slug', blank=True, null=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    discount = models.IntegerField('Discount', null=True, default=0)
    description = models.TextField('Description',)
    is_published = models.BooleanField('Is Published', default=True)
    color = models.ManyToManyField(Color, verbose_name='Color', db_index=True, blank=True, related_name='colors')
    size = models.ManyToManyField(Size, verbose_name='Size', db_index=True, blank=True, related_name='sizes')
    category = models.ForeignKey(ProductCategory, verbose_name='Category',
                                    on_delete=models.CASCADE, db_index=True, related_name='product', blank=True, null=True)
    

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} , {self.category}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{datetime.datetime.now()}')
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("product:product_detail", kwargs={"pk": self.id})

    @property
    def set_discount_price(self):
        if self.discount:
            discount_price = self.price - (self.price*self.discount)/100
            return discount_price



class ProductImage(models.Model):
    image = models.ImageField('Image', upload_to='product_images',)
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='product_image', blank=True, null=True)
    is_published = models.BooleanField('Is Published', default=True)



class Feature(models.Model):
    feature = models.CharField('Feature', max_length=255)
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='feature', blank=True, null=True)



class DataSheet(models.Model):
    data_sheet = models.CharField('Data  Sheet', max_length=255)
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='data_sheet', blank=True, null=True)



class Review(models.Model):
    CHOICES = (
        (5,5),
        (4,4),
        (3,3),
        (2,2),
        (1,1),
    )
    text = models.TextField('Review',)
    users_rating = models.PositiveSmallIntegerField('Rating',choices=CHOICES)
    user = models.ForeignKey(User, verbose_name='User',
                                    on_delete=models.CASCADE, db_index=True, related_name='reviews',  blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='reviews',  blank=True, null=True)
    parent_review = models.ForeignKey('self', verbose_name='Parent Review', on_delete=models.CASCADE, db_index=True, related_name='sub_reviews', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
