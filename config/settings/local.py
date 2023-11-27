# from .base import *
# import os, environ
# from pathlib import Path

# env = environ.Env(
#     DEBUG=(bool, False)
# )

# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('DJANGO_SECRET_KEY')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES":[
#         # "rest_framework.authentication.SessionAuthentication",
#         "api.session_authentication.NoCsrfSessionAuthentication",
#     ],
#     "DEFAULT_PAGINATION_CLASS":"api.pagination.CustomPageNumberPagination",
#     "PAGE_SIZE":10,
# }