from django.shortcuts import render

# Create your views here.
def home_view(request):
    resp = render(request,'tag_filter/home.html')
    return resp

def view_tag(request):
    d1 = {'ex1': "3>6<7"}
    resp = render(request,'tag_filter/tag_ex.html',context=d1)
    return resp