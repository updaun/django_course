from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
from django.views import View

# Create your views here.
def todo_list(request):
   todos = Todo.objects.all() 
   
   search = request.GET.get("search")  # None
   
   if search:
     todo = todo.filter(name_icontains = search)
   
   return render(request,"todo/todo.html", {"todos": todos}) 



def todo_detail(request, pk):
  
  try:
    todo = Todo.objects.get(id=pk)
  except Todo.DoesNotExist: # 예외처리
    return HttpResponse("없는 페이지입니다.", status=484)
    
  
  return render(request, "todo/todo.html", {"todo": todo})
 # return HttpResponse("Todo list")
 
 
def todo_detail_name(request, name):
  todo = Todo.objects.filter(name__icontains=name)
  first = todo.first()
  return render(request, "todo/todo.html", {"todo": todo, "first" : first,})
  


class TodoCreateView(View):
  
  def get(self, request):
    return render(request, "todo/create.html")
  
