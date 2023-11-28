from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer