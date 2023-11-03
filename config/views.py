from django.http.response import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render
import random

def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def hello_world_json(request):
    return JsonResponse({"message": "Hello, World!"})

class RandomNumberTemplateView(TemplateView):
    template_name = "random.html"
    
class RandomNumberView(View):
    def get(Self, request):
        random_number = random.randint(1, 100)
        return render(request, "random.html", {"random":random_number})