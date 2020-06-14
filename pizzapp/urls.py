from django.contrib import admin
from django.urls import path
from .views import adminloginview,adminlogin,\
                   adminhomeview,adminlogout,adminaddpizza,\
                   admindeletepizza,homeview, useradd,\
                   userloginview,userlogin,userhomeview,\
                   userlogout

urlpatterns = [
    #ADMIN
    path('admin/', adminloginview, name='adminloginview'),
    path('adminlogin/', adminlogin),
    path('admin/adminhome/',adminhomeview, name='adminhomeview'),
    path('adminlogout/', adminlogout),
    path('adminaddpizza/', adminaddpizza),
    path('admindeletepizza/<int:pizzaid>', admindeletepizza),

    #USER
    path('', homeview, name='homeview'),
    path('useradd/', useradd),
    path('user/', userloginview,name="userloginview"),
    path('userlogin/', userlogin),
    path('user/userhome/', userhomeview, name='userhomeview'),
    path('userlogout/', userlogout)
]
