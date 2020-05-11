from django.db import models
from django.utils.timezone import timezone
from products.models import Product
from meals.models import Meal

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.last_name)


class ProgramLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    program = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.program.name, self.program.price)


class MealLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.meal.name, self.meal.price)
