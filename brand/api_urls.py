from django.urls import path,include
from rest_framework.routers import DefaultRouter
from brand.apis import BrandViewSet

router = DefaultRouter()
router.register("", BrandViewSet)

urlpatterns = [
    # http://127.0.0.1:8000/api/brand/
    # http://127.0.0.1:8000/api/brand/<int:pk>
    path("", include(router.urls)),
]