# Generated by Django 3.1.7 on 2021-04-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productimage_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Discount'),
        ),
    ]
