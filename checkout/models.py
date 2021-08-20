from django.db import models
from django_countries.fields import CountryField
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Checkout(models.Model):
    first_name = models.CharField('First Name', max_length=31)
    last_name = models.CharField('Last Name', max_length=31)
    email = models.EmailField('Email', max_length=63)
    phone = models.CharField('Price', max_length=15)
    message = models.TextField('Description',)
    country = CountryField()
    company_name = models.CharField('Company Name', blank=True, null=True, max_length=31)
    state = models.CharField('State', max_length=31)
    zip_code = models.CharField('Zip Code', max_length=15)
    name_on_card = models.CharField('Name on Card', max_length=31)
    card_number = models.BigIntegerField('Card Number')
    date = models.DateTimeField('Date')
    security_code = models.IntegerField('Security Code')
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class Wishlist(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='wishlist')


class BasketItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product',
                                    on_delete=models.CASCADE, db_index=True, related_name='basket')
    quantity = models.IntegerField('Quantity', null=True)  
    client = models.ForeignKey(User, verbose_name='User',
                                    on_delete=models.CASCADE, db_index=True, related_name='basket')  