from django.urls import path, include
from .views import *

# 127.0.0.1:8000/todo/
urlpatterns = [
    # Views
    path("create/", TodoCreateView.as_view()), 
    path("list/", TodoListView.as_view()), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", TodoDetailView.as_view()), # 127.0.0.1:8000/todo/list/<int:pk>/ -> pk번 todo를 찾아서 리턴
    path("update/<int:pk>/", TodoUpdateView.as_view()), 
    path("<str:name>/", todo_detail_name), # 127.0.0.1:8000/todo/list/<str:name>/ 
]

