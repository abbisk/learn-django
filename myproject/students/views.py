from .forms import *
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home_view(request):
#     res = HttpResponse("This is students home page")
#     return res

def view_register_student(request):
    if request.method=="GET":
        frmStudent = StudentForm()
        d1 = {'form':frmStudent}
        resp = render(request,'students/register_student.html',context=d1)
        return resp
    elif request.method=="POST":
        pass