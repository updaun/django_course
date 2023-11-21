from django.urls import path
from .apis import *

urlpatterns = [
    path("signup/", SignupAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("logout/", LogoutAPI.as_view()),
]