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

# http://127.0.0.1:8000/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello_world), # 127.0.0.1:8000/
    path("api/auth/", include("users.api_urls")),
    path("api/blog/", include("blog.api_urls")),
    path("api/product/", include("product.api_urls")),
    path("api/brand/", include("brand.api_urls")),
    path("api/todo/", include("todo.api_urls")),
    path("todo/", include("todo.urls")), # 127.0.0.1:8000/todo/
    path("auth/", include("users.urls")), # 127.0.0.1:8000/todo/
    path("random/template/", views.RandomNumberTemplateView.as_view()),
    path("random/view/", views.RandomNumberView.as_view()),
    # 127.0.0.1:8000/api-auth/login/
    # 127.0.0.1:8000/api-auth/logout/ -> session flush cookie
    path('api-auth/', include('rest_framework.urls')),
]