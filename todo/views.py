from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    # return HttpResponse("Todo List")
    todos = Todo.objects.all() # SELECT * FROM todo_todo -> Django Query
    return render(request, "todo.html", {"todos":todos})
