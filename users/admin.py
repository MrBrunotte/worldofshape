from django.contrib import admin
from .models import Profile

# Register your models here.
"""
register the profile model so we can use it in the admin panel
"""
admin.site.register(Profile)
