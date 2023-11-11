from django.urls import path,include
from .views import *



 

# 8000/todo/

urlpatterns = [
    #VIEWS
    path("create/", TodoCreateView.as_view()),
    path("list/", todo_list), #127.0.0.1:8000/todo/list/
    path("<int:pk>/", todo_detail), #127.0.0.1:8000/todo/<int:pk>/
    path("<str:name>/", todo_detail_name),
]

# url.py (라우팅) -> views.py(로직) -> html(템플릿)

