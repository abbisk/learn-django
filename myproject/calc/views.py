from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(required):
    res = HttpResponse("<h1>Welcome to the calculator homepage</h1>")
    return res