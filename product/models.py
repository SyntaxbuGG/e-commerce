import os

from django.db import models

from base.models import TimeStampedModel
from category.models import Category
from account.models import User
from .managers import ProductManager





class Color(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Size(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Product(TimeStampedModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    color = models.ManyToManyField(Color, blank=True,null=True)
    size = models.ManyToManyField(Size, blank=True, null=True)


    custom = ProductManager()
    objects = models.Manager()
    def __str__(self):
        return self.title

def product_image_upload(instance, filename):
    # Get the category of the product
    product_id = instance.product.id
    # Generate the path for the image
    path = os.path.join('product/images', str(product_id),filename)
    return path


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_upload)

    def __str__(self):
        return self.product.title
