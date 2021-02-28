from django.shortcuts import render

# Create your views here.
def home_view(request):
    resp = render(request,'tag_filter/home.html')
    return resp