from django.db import models
from django.urls import reverse

# Create your models here.


class Meal(models.Model):
    """
    This is the database for the meal and diet plans
    """
    name = models.CharField(max_length=50, default='')
    name2 = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    full_description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self, **kwargs):
        return reverse('meal-detail', kwargs={'pk': self.pk})


class MealProgram(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(default='')

    def __str__(self):
        return self.name
