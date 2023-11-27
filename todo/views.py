from django.shortcuts import render
from django.views import View
from .models import Todo
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated


def todo_list(request):
    # return HttpResponse("Todo list")
    todos = Todo.objects.all() # Django Query # 모든 데이터 -> queryset [Todo Object ,Todo Object, Todo Object]
   
    search = request.GET.get("search") # None
    # search = request.GET["search"] # KeyError: 'search' 지양 -> server error 500
    if search:
        todos = todos.filter(name__icontains=search)

    return render(request, "todo/todo.html", {"todos": todos})


def todo_detail(request, pk):
    # todo = Todo.objects.get(pk=pk)
    # try:
    #     todo = Todo.objects.get(id=pk) # -> Todo Object
    # except Todo.DoesNotExist: # 예외처리
    #     return HttpResponse("없는 페이지입니다.", status=404)
    todo = Todo.objects.filter(id=pk).first() # unique 빈 쿼리셋에 fisrt => None
    if todo is None:
        return HttpResponse("없는 페이지입니다.", status=404)
    return render(request, "todo/todo.html", {"todo": todo})


def todo_detail_name(request, name):
    todo = Todo.objects.filter(name__icontains=name) # queryset
    first = todo.first()
    last =  todo.last()
    return render(request, "todo/todo.html", {"todo": todo, "first": first, "last": last})


class TodoCreateView(View):

    def get(self, request):
        return render(request, "todo/create.html")
    

class TodoListView(LoginRequiredMixin, View):

    def get(self, request):
        # todos = Todo.objects.all()
        return render(request, "todo/list2.html")
    

class TodoDetailView(View):

    def get(self, request, pk):
        return render(request, "todo/detail.html")
    

class TodoUpdateView(View):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        return render(request, "todo/update.html")