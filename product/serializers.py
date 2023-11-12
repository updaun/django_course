from rest_framework import serializers
from product.models import Product
from brand.serializers import BrandSerializer


# 생성용 serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

# 읽기용 serializer
class ProductReadSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"