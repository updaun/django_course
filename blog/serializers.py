from rest_framework import serializers
from blog.models import Blog
from category.models import Category
from category.serializers import CategorySerializer

class BlogSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, required=False)
    class Meta:
        model = Blog
        exclude = (
            "view", #조회수 주작 방지
            "hidden",
            )
        # fields = "__all__"


class BlogReadSerializer(serializers.ModelSerializer):
    # nested serializer
    category = CategorySerializer(many=True, read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"