from django.contrib import admin
from .models import Blog

# admin.site.register(Blog) # 어드민 홈페이지에 blog 카테고리 추가

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "view",
    )