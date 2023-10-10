from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def todo_list(request):
    # return httpresponse("todo list")
    todos = Todo.objects.all() #select all from todo_todo;
    return render(request, "todo.html", {"todos":todos})
    # 이거 뭐라고 했었는데 todos. ㅁㄴㅇㄻㄴㅇㄹ라고 함.