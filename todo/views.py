from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo.html", {"todos": todos})