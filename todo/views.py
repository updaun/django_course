from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    # return HttpResponse("Todo List")
    todos = Todo.objects.all() # SELECT * FROM todo_todo -> 모든 데이터 -> Django Queryset[Todo Objects]
    
    search = request.GET.get("search") # None
    # search = request.GET.["search"] # Key Error(500) -> 지양
    if search:
        todos = todos.filter(name__icontains=search)
    
    return render(request, "todo/todo.html", {"todos": todos})

def todo_detail(request, pk):
    # try:
    #     todo = Todo.objects.get(id=pk) # -> Todo Object
    # except Todo.DoesNotExist:
    #     return HttpResponse("없는 페이지입니다.", status=404) # 예외처리
    
    todo = Todo.objects.filter(id=pk).first() #unique
    if todo is None:
        return HttpResponse("없는 페이지입니다.", status=404) # 예외처리  
    return render(request, "todo/todo.html", {"todo": todo})

def todo_detail_name(request, name):
    todo = Todo.objects.filter(name__icontains=name) # Queryset
    first = todo.first()
    last = todo.last() 
    return render(request, "todo/todo.html", {"todo": todo, "first": first, "last": last})


