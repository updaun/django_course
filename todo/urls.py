from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.todo_list),
    path("<int:pk>/", views.todo_detail),
    # ~/todo/<int:pk>/ pk = 135 135번 todo를 찾아 리턴
    path("<str:name>/", views.todo_detail_name),
    #<str:name> name = 공부
]
