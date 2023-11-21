from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from api.authentication import IsAuthenticatedCustom

class TodoCreateAPI(APIView):
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        # return Json data
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

class TodoListAPI(APIView):
    
    def get(self, request):
        todos = Todo.objects.all().order_by("-created_at")
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class TodoRetrieveAPI(APIView):
    
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 Todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

class TodoUpdateAPI(APIView):
    
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 Todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(TodoSerializer(todo).data)
    
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 Todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(TodoSerializer(todo).data)

class TodoDeleteAPI(APIView):
    
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 Todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(data={"data":"OK"}, status=status.HTTP_204_NO_CONTENT)

# using generics
class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer
    

class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at")
    
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedCustom,)

    # 본인의 todo만 조회, listapi, retrieveapi, destroyapi
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user)

    # 상세조회 retrieve
    # todo/100/
    # [200, 203, 204]   100번을 요청? -> 404 Not Found

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return instance

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perfrom_update(self, serializer):
        instance = serializer.save(user=self.request.user)
        return instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        todo = self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)




