from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import PizzaModel
from django.contrib.auth.models import User
from .models import UserModel

import datetime
# Create your views here.

#Admin
def adminloginview(request):
    return render(request,"pizzapp/adminlogin.html")
    

def adminlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user and user.username=="admin":
        login(request, user)
        return redirect('adminhomeview')
    else:
        # you cant : messages.add_message(request, messages.ERROR, "Invalid creadentials")
        messages.error(request, 'Invalid credentials')
        return redirect(request.META['HTTP_REFERER'])


def adminhomeview(request):
    pizzas = PizzaModel.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzapp/adminhome.html', context)

def adminlogout(request):
    logout(request)
    return redirect('adminloginview')

def adminaddpizza(request):
    name = request.POST['name']
    price = request.POST['price']
    pizza = PizzaModel(name=name, price=price)
    pizza.save()
    return redirect(request.META['HTTP_REFERER'])

def admindeletepizza(request, pizzaid):
    PizzaModel.objects.filter(id=pizzaid).delete()
    return redirect(request.META['HTTP_REFERER'])

def useradd(request):
    username = request.POST['username']
    password = request.POST['password']
    phone = request.POST['phone']
    checkuser = User.objects.filter(username=username).exists()
    
    if checkuser:
        #User exists
        messages.error(request, "User exists")
        return redirect(request.META['HTTP_REFERER'])
        # you can : return redirect('homeview')
    else:
        #User does not exists
        user = User.objects.create_user(username=username, password=password)
        UserModel(userid = user.id, phone=phone).save()
        messages.success(request, "User created successfully")
        return redirect(request.META['HTTP_REFERER'])
        # you can : return redirect('homeview)
    

#USERS
def homeview(request):
    return render(request, 'pizzapp/home.html')


def userloginview(request):
    return render(request, 'pizzapp/userlogin.html')


def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    # check if user exists
    if user:
        login(request, user)
        return redirect('userhomeview')
    else:
        messages.error(request, "User does not exists")
        return redirect(request.META['HTTP_REFERER'])
        

def userhomeview(request):
    # Get account's user dynamically
    username = request.user.username
    context = {'username': username, 'pizzas': PizzaModel.objects.all()}
    return render(request, 'pizzapp/userhomeview.html', context)

def userlogout(request):
    logout(request)
    return redirect("userloginview")