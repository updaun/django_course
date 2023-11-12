from rest_framework import viewsets
from product.models import Product
from product.serializers import ProductSerializer, ProductReadSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    read_serializer_class = ProductReadSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return self.read_serializer_class
        else:
            return self.serializer_class