from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("Welcome to Django World")


urlpatterns = [
    path("", home),
]
