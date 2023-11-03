from django.urls import path
from .views import todo_list

# 127.0.0.1:8000/todo/
urlpatterns = [
    path("list/", todo_list), # 127.0.0.1:8000/todo/list/
]