from django.urls import path
from .apis import *
from .views import *

urlpatterns = [
    path("create/", TodoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
    path("<int:pk>/", todo_detail),
    # ~/todo/<int:pk>/ pk = 135 135번 todo를 찾아 리턴
    path("<str:name>/", todo_detail_name),
    #<str:name> name = 공부
]
