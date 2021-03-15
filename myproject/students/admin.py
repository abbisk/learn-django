from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Student,Course,PaymentDetails,EducationDetails

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(PaymentDetails)
admin.site.register(EducationDetails)