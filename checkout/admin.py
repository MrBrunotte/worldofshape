from django.contrib import admin
from .models import Order, ProductLineItem, MealLineItem


class ProductLineAdminInline(admin.TabularInline):
    model = ProductLineItem


class MealineAdminInline(admin.TabularInline):
    model = MealLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductLineAdminInline, MealineAdminInline)


admin.site.register(Order, OrderAdmin)
