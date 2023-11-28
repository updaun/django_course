from django.shortcuts import render
from django.views import View
from .models import Blog
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

# http://127.0.0.1:8000/blog/create/
class BlogCreateView(View):
    def get(self, request):
        return render(request, "blog/create.html")


class BlogDetailView(View):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return HttpResponse("<h1> 존재하지 않는 블로그입니다. </h1>")
        return render(request, "blog/detail.html", {"blog": blog})
    

class BlogUpdateView(View):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return HttpResponse("<h1> 존재하지 않는 블로그입니다. </h1>")
    
        if blog.user != request.user:
            return HttpResponse("<h1> 권한이 없습니다. </h1>")

        return render(request, "blog/update.html", {"blog": blog})


class MyBlogListView(View):
    def get(self, request):
        return render(request, "blog/myblog.html")