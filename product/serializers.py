from rest_framework import serializers
from product.models import Product
from brand.serializers import BrandSerializers
from brand.models import Brand

#생성용 Serializer
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all)
    class Meta:
        model = Product
        fields = "__all__"
        
#읽기용 Serializer
class ProductReadSerializer(serializers.ModelSerializer):
    brand = BrandSerializers(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"