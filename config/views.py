from django.http.response import HttpResponse,JsonResponse

#function-basic view
def hello_world(request):
    return HttpResponse("<h1>Hello, world!!</h1>")

#function-basic view
def hello_world_jason(request):
    return JsonResponse({"message":"Hello,World!"})
