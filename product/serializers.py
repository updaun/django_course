from rest_framework import serializers
from product.models import Product
from brand.serializers import BrandSerializer

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class ProductReadSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"