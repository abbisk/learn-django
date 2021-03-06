"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import include


def sum(request,no1,no2):
    res = no1+no2
    resp =  HttpResponse("Sum of no = " +str(res))
    return resp

def multiply(request, no1,no2):
    res = no1*no2
    resp = HttpResponse("Product of no = " +str(res))
    return resp

def my_view(request):
    resp = HttpResponse("<h1>Welcome to Homepage</h1>")
    return resp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:no1>/<int:no2>/', sum),
    path('multiply/<int:no1>/<int:no2>/', multiply),
    path('',my_view),
    path('calc/', include('calc.urls')),
    path('students/', include('students.urls')),
    path('tag/', include('tag_filter.urls')),
    path('websecurity/', include('websecurity.urls')),


]