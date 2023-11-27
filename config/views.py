from django.http.response import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView, View
from django.shortcuts import render
import random

def hello_World(request):
    return HttpResponse("Hello, world!")

def hello_world_json(request):
    return JsonResponse({"message": "hello, world!"})

class RandomNumberTemplateView(TemplateView):
    template_name = "random.html"

class RandomNumberView(View):
    def get(self, request):
        random_number = random.randint(1, 100)
        return render(request, "random.html", {"random" : random_number})

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")