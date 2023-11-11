from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello_world), # 127.0.0.1:8000/
    path("api/todo/", include("todo.api_urls")),
    path("todo/", include("todo.urls")), # 127.0.0.1:8000/todo/
    path("random/template/", views.RandomNumberTemplateView.as_view()),
    path("random/view/", views.RandomNumberView.as_view()),
    # 127.0.0.1:8000/api-auth/login/
    # 127.0.0.1:8000/api-auth/logout/ -> session flush cookie
    path('api-auth/', include('rest_framework.urls')),
]
