from django.urls import path
from .views import *

urlpatterns = [
    path("create/", BlogCreateView.as_view()),
    path("<int:pk>/", BlogDetailView.as_view()),
    path("update/<int:pk>/", BlogUpdateView.as_view()),
    path("my/", MyBlogListView.as_view()),
]
