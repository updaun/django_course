from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(request):
   todos = Todo.objects.all() 
   return render(request,"todo.html", {"todos": todos}) 


 # return HttpResponse("Todo list")