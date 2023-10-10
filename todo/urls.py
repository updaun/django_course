from django.urls import path
from .views import todo_list

urlpatterns = [
    path("", todo_list)
]
