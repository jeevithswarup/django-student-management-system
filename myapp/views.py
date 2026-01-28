from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
   if request.user.is_authenticated:
        return redirect('zomato_home')
   if request.method =='POST':
      user_name=request.POST.get('user_name')
      password=request.POST.get('password')
      if User.objects.filter(username=user_name).exists():
            messages.error(request, "⚠️ Username already exists, try another one.")   
            return redirect('/register')     
      User.objects.create_user(
      username=user_name,
      password=password,
     )
      return redirect('/')
   return render(request,'register.html')

def login_page(request):
   if request.user.is_authenticated:
        return redirect('zomato_home')
   if request.method == "POST":
      user_name= request.POST. get('user_name')
      password= request.POST.get('password')

      user=authenticate(request,username=user_name,password=password)
      if user is not None:
       login(request,user)
       return redirect('/zomato/')
      else:
       return render(request,'myfirst.html',{"error":"invalid username or password"})
   return render(request,"myfirst.html")
def logout_page(request):
   logout(request)
   return redirect('/')
@login_required
def zomato_home(request):
   return render(request,"zomato.html")



