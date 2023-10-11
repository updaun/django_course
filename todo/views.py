from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    # return HttpResponse("Todo list")
    todos = Todo.objects.all()
    return render(request, "todo.html", {"todos": todos})