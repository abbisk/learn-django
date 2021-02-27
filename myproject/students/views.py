from .forms import *
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view_register_student(request):
    if request.method=="GET":
        frmStudent = StudentForm()
        d1 = {'form':frmStudent}
        resp = render(request,'students/register_student.html',context=d1)
        return resp
    elif request.method=="POST":
        frmStudent = StudentForm(request.POST)
        if frmStudent.is_valid():
            s = frmStudent.save()
            resp = HttpResponse("Student added Successfully")
            return resp

        else:
            pass


def view_show_all_students(request):
    all_stu = Student.objects.all()
    d1={'allstudents':all_stu}
    resp = render(request,'students/all_students.html',context=d1)
    return resp

def view_course_by_student_id(request,id):
    d1={}
    resp = render(request,'students/student_wise_courses.html',context=d1)
    return resp