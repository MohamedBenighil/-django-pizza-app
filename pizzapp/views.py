from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def adminloginview(request):
    return render(request,"pizzapp/adminlogin.html")
    

def adminlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user and user.username=="admin":
        login(request, user)
        return redirect('adminhome')
    else:
        #messages.add_message(request, messages.ERROR, "Invalid creadentials")
        messages.error(request, 'Invalid credentials')
        return redirect(request.META['HTTP_REFERER'])


def adminhomeview(request):
    return render(request, 'pizzapp/adminhome.html')


def userauth(request):
    return render(request,'pizzapp/userauth.html')

