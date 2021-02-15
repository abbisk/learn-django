from django.db import models
from django.core.validators import ValidationError
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    # students=models.ManyToManyField(Student,blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=500,blank=True,null=True)
    mobile=models.CharField(max_length=15)
    emailid=models.EmailField(max_length=100)
    date_of_birth=models.DateField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)
    courses=models.ManyToManyField(Course)
    def __str__(self):
        return self.name
    

    
def check_payment_amount(value):
    if value<=0:
        raise ValidationError("Non Zero or Negative Values are not allowed")
class PaymentDetails(models.Model):
    amount=models.IntegerField( validators=[check_payment_amount,])
    payment_mode=models.CharField(max_length=20,choices=[('cash','Cash'),('dd','DD'),('paytm','PayTM')])
    payment_ref_no=models.CharField(max_length=100,null=True,blank=True)
    date_of_payment=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.amount
class EducationDetails(models.Model):
    higher_education=models.CharField(max_length=100,choices=[('10th','10th'),('12th','12th'),('Graduation','Graduation')])
    year_of_education=models.IntegerField(blank=True,null=True)
    student=models.OneToOneField(Student,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):      
        return self.higher_education

    

