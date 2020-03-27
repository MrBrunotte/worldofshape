from django.db import models

# Create your models here.


class Product(models.Model):
    """
    This is the database for the products/programs
    We specify the columns that will be in the tables in our db
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
