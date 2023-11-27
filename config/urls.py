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
from django.urls import path, include
from . import views

# from .views import (
#     hello_world_json, 
#     hello_World, 
#     RandomNumberView,
#     )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("users.api_urls")),
    path("api/category/", include("category.api_ruls")),
    path("auth/", include("users.urls")),
    path("api/blog/", include("blog.api_urls")),
    path("", HomeView.as_view()),
    path("api/product/", include("product.api_urls")),
    path("api/brand/", include("brand.api_urls")),
    # path("json/", views.hello_world_json),
    path("api/todo/", include("todo.api_urls")),
    path("todo/", include("todo.urls")),
    path("random/template/", views.RandomNumberTemplateView.as_view()), #클래스일 때는 이걸 해줘야함!!!
    path("random/view/", views.RandomNumberView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
