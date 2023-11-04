from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


class TOdoCreateAPI(APIView):
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
    
    
    
class TodoListAPI(APIView):
    
    def get(self, request):
        todos = Todo.objects.all() # Queryssset = object list
        serializer = TodoSerializer(todos, many=True)
        
        return Response(serializer.data)
        #return Response({"data = hi"})