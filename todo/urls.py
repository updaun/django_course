from django.urls import path, include
from .views import *


# 127.0.0.1:8000/todo/
urlpatterns = [
    # VIEWS
    path("update/<int:pk>/", TodoUpdateView.as_view()), 
    path("create/", TodoCreateView.as_view()),
    path("list/", TodoListView.as_view()), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", TodoDetailView.as_view()), # 127.0.0.1:8000/todo/<int:pk>/ pk = 135  135번 todo를 찾아서 리턴
    path("<str:name>/", todo_detail), # 127.0.0.1:8000/todo/<str:name>/ name = 공부  135번 todo를 찾아서 리턴
]

# urls.py (라우팅) -> views.py(로직) -> ~~.html(템플릿)