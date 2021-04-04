from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    mobileno= models.CharField(max_length=15)
    address=models.TextField(max_length=500,blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    pic=models.ImageField(blank=True,null=True,upload_to="user_pic")
    user= models.OneToOneField(User,on_delete=models.CASCADE)
