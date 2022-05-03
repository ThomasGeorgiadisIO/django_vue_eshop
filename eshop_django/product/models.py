from unicodedata import category, name
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)