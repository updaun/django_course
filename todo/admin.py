from django.contrib import admin
from .models import Todo
from django.contrib.sessions.models import Session

admin.site.register(Session)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
        "created_at",
        "updated_at",
    )