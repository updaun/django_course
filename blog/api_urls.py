from django.urls import path, include
from blog.apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)

urlpatterns = [
    path("my/", MyBlogListAPI.as_view()),
    path("", include(router.urls)),
]