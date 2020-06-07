from django.contrib import admin
from django.urls import path
from .views import adminloginview,userauth,adminlogin,adminhomeview

urlpatterns = [
    path('admin/', adminloginview),
    path('adminlogin/', adminlogin),
    path('admin/adminhome/',adminhomeview, name='adminhome'),
    path('', userauth)
]
