from django.urls import path, include
from .apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 127.0.0.1:8000/api/todo/viewsets/<int:pk>/
router.register("", TodoViewSet)

# 127.0.0.1:8000/todo/
urlpatterns = [
    # APIS
    # 127.0.0.1:8000/todo/viewsets/
    path("viewsets/", include(router.urls)),
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
]
