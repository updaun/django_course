from django.urls import path, include
from .views import *

# 127.0.0.1:8000/todo/
urlpatterns = [
    #<str:name> name = 공부
    #views
    path("create/", TodoCreateView.as_view()),
    # path("<int:pk>/", TodoDetailView.as_view()),
    # path("list/", TodoListView.as_view()),
    # path("update/", TodoUpdateView.as_view()),
    
    # ~/todo/<int:pk>/ pk = 135 135번 todo를 찾아 리턴
    
    path("list/", todo_list),
    path("<int:pk>/", todo_detail),
    path("<str:name>/", todo_detail_name),
]

