from django.urls import path
from . import views
# 127.0.0.1:8000/todo/
urlpatterns = [
    path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", views.todo_detail), # 127.0.0.1:8000/todo/list/<int:pk>/ -> pk번 todo를 찾아서 리턴
    path("<str:name>/", views.todo_detail_name), # 127.0.0.1:8000/todo/list/<str:name>/ 
]

