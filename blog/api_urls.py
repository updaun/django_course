from django.urls import path, include
from blog.apis import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)


urlpatterns = [
    # http://127.0.0.1:8000/api/blog/
    path("", include(router.urls)),
]