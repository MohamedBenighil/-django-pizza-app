from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import PizzaModel


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
        return redirect('adminhome')
    else:
        #messages.add_message(request, messages.ERROR, "Invalid creadentials")
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




#USERS
def userauth(request):
    return redirect(request,'pizzapp/userauth.html')

