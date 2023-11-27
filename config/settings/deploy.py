from .base import *

def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-7!t$i*_145_k-+dsji2j5vuwx&s880)=br*__rxvz5cjyh%2('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': read_secret('POSTGRES_DB'),
        'USER': read_secret('POSTGRES_USER'),
        'PASSWORD': read_secret('POSTGRES_PASSWORD'),
        'HOST': 'postgresdb',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":[
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS":"api.pagination.CustomPageNumberPagination",
    "PAGE_SIZE":10,
}