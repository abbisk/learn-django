#base Url: http://127.0.0.1:8000/calc/
from django.urls import path
from django.http import HttpResponse

def home_view(required):
    res = HttpResponse("<h1>Welcome to the calculator homepage</h1>")
    return res

urlpatterns = [
    path('', home_view)
]