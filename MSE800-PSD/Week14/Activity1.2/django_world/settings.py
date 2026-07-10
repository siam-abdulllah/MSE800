from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-dev-key-only"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = []

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "django_world.urls"

TEMPLATES = []

WSGI_APPLICATION = "django_world.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
