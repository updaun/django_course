from django.urls import path
from .apis import *
from .views import *
# 127.0.0.1:8000/todo/
urlpatterns = [
    path("generics/", TodoGenericsListCreateAPI.as_view()),
    path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view()),
    path("generics/create/", TodoGenericsCreateAPI.as_view()),
    path("generics/list/", TodoGenericsListAPI.as_view()),
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view()),
    path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view()),
    path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view()),
    path("create/", TodoCreateAPI.as_view()), 
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
    path("list/", todo_list), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", todo_detail), # 127.0.0.1:8000/todo/list/<int:pk>/ -> pk번 todo를 찾아서 리턴
    path("<str:name>/", todo_detail_name), # 127.0.0.1:8000/todo/list/<str:name>/ 
]

