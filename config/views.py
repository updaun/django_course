from django.http.response import HttpResponse,JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render
import random


def helloworld(request):
    return HttpResponse("Hello, world!")

def helloworld_json(request):
    return HttpResponse({"message : Hello, world!"})

class RandomNumberTemplateView(TemplateView):
    template_name = "random.html"
    
class RandomNumberView(View):
    def get(self, request):
        random_number = random.randint(1, 100)
        return render(request, "random.html", {"random" : random_number})