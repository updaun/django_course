from django.urls import path, include
from blog.apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)


urlpatterns = [
    # http://127.0.0.1:8000/api/blog/
    path("my/", MyBlogListAPI.as_view()),
    path("", include(router.urls)),
]