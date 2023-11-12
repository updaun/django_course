from rest_framework import viewsets
from brand.models import Brand
from brand.serializers import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by("-id")
    serializer_class = BrandSerializer