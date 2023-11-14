from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import *

router = DefaultRouter()
router.register("", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]