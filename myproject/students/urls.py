#base Url: http://127.0.0.1:8000/students/
from django.urls import path
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('',home_view),
    path('register', view_register_student),
    path('showall', view_show_all_students),
    path('showall', view_course_by_student_id),
]