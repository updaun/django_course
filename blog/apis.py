from rest_framework import viewsets
from blog.models import Blog
from blog.serializer import BlogSerializer, BlogReadSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    read_serializer_class =BlogReadSerializer
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return self.read_serializer_class
        return self.serializer_class