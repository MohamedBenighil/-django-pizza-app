from django.contrib import admin
from django.urls import path
from .views import adminloginview,userauth,adminlogin,adminhomeview,adminlogout,adminaddpizza,admindeletepizza

urlpatterns = [
    path('admin/', adminloginview, name='adminloginview'),
    path('adminlogin/', adminlogin),
    path('admin/adminhome/',adminhomeview, name='adminhome'),
    path('adminlogout/', adminlogout),
    path('adminaddpizza/', adminaddpizza),
    path('admindeletepizza/<int:pizzaid>', admindeletepizza)
]
