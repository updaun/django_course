from django.urls import path
from .apis import *

# /api/auth/
urlpatterns = [
    path("signup/", SignupAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("logout/", LogoutAPI.as_view()),
]