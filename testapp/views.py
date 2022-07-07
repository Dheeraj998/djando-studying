from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
# Create your views here.


# def demo(request):
#   return HttpResponse("Hello World")


def demo(request):
  #passing value
  name="Dheeraj"
  return render(request,'index.html',{'obj':name})
#multiple views
def about(request):
  return render(request,'about.html')  
def profile(request):
  return HttpResponse('profile')  

#passing data from one page to another
def addition(request):
  number1=int(request.GET['num1'])
  number2=int(request.GET['num2'])
  result=number1+number2
  return render(request,'about.html',{'result':result})  
@api_view(['POST'])
def login(request):
  username1=request.data['username']  
  password1=request.data['password']  
  user_name=User.objects.get(username=username1)
  if User.objects.filter(username=username1).exists():
    pass_word=authenticate(username=username1,password=password1)

    return Response ('login success')
  

  print(user_name)
  
  #  if user_name==username:
  #     print( "login")
def renderhtmlPage(request):
  return render(request,'index.html')
def loginHtml(request):
  if request.method == 'POST':
    username=request.POST.get('userr')
    password=request.POST.get('pass')
    user_object=Login.objects.get(username=username,password=password)
    if Login.objects.filter(username=username,password=password).exists():
      return redirect(renderhtmlPage)