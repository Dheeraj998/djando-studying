from django.http import HttpResponse
from django.shortcuts import render

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