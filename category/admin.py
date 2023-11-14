from django.contrib import admin
from category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass