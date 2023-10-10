from django.http.response import HttpResponse, JsonResponse

def hello_World(request):
    return HttpResponse("Hello, world!")

def hello_world_json(request):
    return JsonResponse({"message": "hello, world!"})