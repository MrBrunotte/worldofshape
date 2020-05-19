from django.db import models
from django.urls import reverse
from .forms import WeightLossAnalysisForm

# Create your models here.


class Product(models.Model):
    """
    This is the database for the products/programs
    We specify the columns that will be in the tables in our db
    """

    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    full_description = models.TextField(default='')
    full_description_2 = models.TextField(default='')
    full_description_3 = models.TextField(default='')
    full_description_4 = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(default='')
    #image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def get_absolute_url(self, **kwargs):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Program(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(default='')
    #image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
