from django.urls import path
from . import views

urlpatterns = [
    path("list/",views.todo_list), #127.0.0.1:8000/todo/list/
    path("<int:pk>/",views.todo_detail), #127.0.0.1:8000/todo/<int:pk>/
    path("<str:name>/",views.todo_detail_name),
]

# url.py (라우팅) -> views.py(로직) -> html(템플릿)

