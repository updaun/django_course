"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http.response import HttpResponse,JsonResponse
from .views import hello_world,hello_world_jason
#views.py->views에서(=from) hello_world, helloworld_json을 데려온다(=import한다)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",hello_world),
    path("json/",hello_world_jason)
]
