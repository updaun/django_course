from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views import View

# Create your views here.
def todo_list(request):
    # return httpresponse("todo list")
    todos = Todo.objects.all() #select all from todo_todo;
    # Django Query -> query set (=list of todo object)
    search = request.GET.get("search") # => default = None
    # default value setting => ex) ("search", "")
    # search = request.Get["search"] key not found -> server error 500
    if search:
        todos = todos.filter(name__icontains = search)
    
    return render(request, "todo/todo.html", {"todos":todos})
    # 이거 뭐라고 했었는데 todos. ㅁㄴㅇㄻㄴㅇㄹ라고 함.

def todo_detail(request, pk):
    # todo = Todo.objects.get(pk=pk) 이렇게 해도 됨.
    # try:
    #     todo = Todo.objects.get(id=pk) #해당하는 키 없을 경우 에러
    #     # Todo Object
    # except Todo.DoesNotExist: #예외 처리
    #     return HttpResponse("없는 페이지입니다.", status=404)
    todo = Todo.objects.filter(id=pk).first() #unique data
    #get은 예외처리가 필수
    #first 이전까지는 쿼리. 빈 쿼리셋 first시 None return
    if todo is None: #위의 try 문과 같음.
        return HttpResponse("없는 페이지입니다.", status = 404)
    return render(request, "todo/todo.html", {"todo": todo})

def todo_detail_name(request, name):
    todo = Todo.objects.filter(name__icontains = name)
    #query set return
    # first = Todo.objects.filter(name__icontains=name).first()
    first = todo.first()
    # last = Todo.objects.filter(name__icontains=name).first()
    last = todo.last()#위와 같다.
    return render(request, "todo/todo.html", {"todo": todo, "first": first, "last":last})


class TodoCreateView(View):
    
    def get(self, request):
        return render(request, "todo/create.html")

class TodoListView(View):

    def get(self, request):
        # todos = Todo.objects.all()
        return render(request, "todo/list2.html")


class TodoDetailView(View):

    def get(self, request, pk):
        return render(request, "todo/detail.html")


class TodoUpdateView(View):

    def get(self, request, pk):
        return render(request, "todo/update.html")
    