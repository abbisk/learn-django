from django.shortcuts import render
from .models import *
# from .forms import *

# Create your views here.
def view_home(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/home.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

def view_login(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/login.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

def view_logout(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/logout.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

#register
def view_register(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/registration.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

#profile
def view_profile(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/profile.html',context=d1)
        return resp

    elif request.method=="POST":
        pass
 

 #buyer1
def view_buyer1(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/securebuyer1.html',context=d1)
        return resp

    elif request.method=="POST":
        pass


#buyer2
def view_buyer2(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/securebuyer2.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

#seller1
def view_seller1(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/secureseller1.html',context=d1)
        return resp

    elif request.method=="POST":
        pass


#seller2
def view_seller2(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/secureseller2.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

#unsecure1
def view_unsecure1(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/unsecure1.html',context=d1)
        return resp

    elif request.method=="POST":
        pass

#unsecure2
def view_unsecure2(request):
    if request.method=="GET":
        d1={}
        resp = render(request,'websecurity/unsecure2.html',context=d1)
        return resp

    elif request.method=="POST":
        pass