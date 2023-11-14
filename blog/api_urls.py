from django.urls import path, include
from blog.apis import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
]