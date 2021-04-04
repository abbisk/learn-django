#base Url: http://127.0.0.1:8000/security/
from django.urls import path
from .views import *

urlpatterns = [
    path('',view_home,name='home'),
    path('login/',view_login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('register/',view_register,name='register'),
    path('profile/',view_profile,name='profile'),
    path('buyer1/',view_buyer1,name='buyer1'),
    path('buyer2/',view_buyer2,name='buyer2'),
    path('seller1/',view_seller1,name='seller1'),
    path('seller2/',view_seller2,name='seller2'),
    path('unsecure1/',view_unsecure1,name='unsecure1'),
    path('unsecure2/',view_unsecure2,name='unsecure2'),
]