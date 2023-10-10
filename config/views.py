from django.http.response import HttpResponse, JsonResponse

def hello_world(request):
    return HttpResponse("Hello world!")

def hello_world_json(request):
    return JsonResponse({"message" : "Hello world!"})