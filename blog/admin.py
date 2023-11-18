from django.contrib import admin
from blog.models import Blog

# Register your models here.
@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "view",
    )