from django.urls import path, include
from .views import *

# 127.0.0.1:8000/todo/
urlpatterns = [
    # Views
    path("create/", TodoCreateView.as_view()), 
    path("list/", todo_list), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", todo_detail), # 127.0.0.1:8000/todo/list/<int:pk>/ -> pk번 todo를 찾아서 리턴
    path("<str:name>/", todo_detail_name), # 127.0.0.1:8000/todo/list/<str:name>/ 
]

