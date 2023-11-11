from django.urls import path,include
from .apis import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TodoViewSet)
 

# 8000/todo/

urlpatterns = [
    #APIS
    #8000:/todo/viewsets/
    path("viewsets/", include(router.urls)),
    path("generics/", TodoGenericsListCreateAPI.as_view()),
    path("generics/<int:pk>", TodoGenericsRetrieveUpdateDeleteAPI.as_view()),
    path("generics/create/", TodoGenericsCreateAPI.as_view()),
    path("generics/list/", TodoGenericsListApi.as_view()),
    path("generics/retrieve/<int:pk>",  TodoGenericsRetrieveAPI.as_view()),
    path("generics/update/<int:pk>",  TodoGenericsUpdateAPI.as_view()),
    path("generics/delet/<int:pk>",  TodoGenericsDeleteAPI.as_view()),
    path("create/", TOdoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
  
]

# url.py (라우팅) -> views.py(로직) -> html(템플릿)

