from django.urls import path, include
from rest_framework.routers import DefaultRouter
from brand.apis import *

router = DefaultRouter()
router.register("", BrandViewSet)

urlpatterns = [
    path("", include(router.urls)),
]