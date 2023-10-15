from django.http.response import HttpResponse,JsonResponse




def helloworld(request):
    return HttpResponse("Hello, world!")

def helloworld_json(request):
    return HttpResponse({"message : Hello, world!"})