#base Url: http://127.0.0.1:8000/calc/
from django.urls import path
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('register', view_register_student)
]