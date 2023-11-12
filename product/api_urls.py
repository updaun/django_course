from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.apis import *


router = DefaultRouter()
router.register("", ProductViewSet)

urlpatterns = [
    # http://127.0.0.1:8000/api/product/
    # http://127.0.0.1:8000/api/product/<int:pk>/
    path("", include(router.urls)),
]