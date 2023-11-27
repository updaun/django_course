from rest_framework import viewsets, generics
from blog.models import Blog
from blog.serializers import BlogSerializer, BlogReadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    read_serializer_class = BlogReadSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return self.read_serializer_class
        return self.serializer_class
    
    def get_queryset(self):
        queryset = self.queryset

        # 카테고리 필터링
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        # 카테고리는 이름으로도 필터링 하고자 한다.
        category_name = self.request.query_params.get("category_name")
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        # 타이틀 필터링
        title = self.request.query_params.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyBlogListAPI(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogReadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        # 내 블로그만 필터링
        queryset = queryset.filter(user=self.request.user)
        return queryset