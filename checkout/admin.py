from django.contrib import admin
from .models import Order, ProgramLineItem, MealLineItem


class ProgramLineAdminInline(admin.TabularInline):
    model = ProgramLineItem


class MealineAdminInline(admin.TabularInline):
    model = MealLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProgramLineAdminInline, MealineAdminInline)


admin.site.register(Order, OrderAdmin)
