from django.urls import path
from .apis import *

urlpatterns = [
    path("", CategoryListAPI.as_view()),
]