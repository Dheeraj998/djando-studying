from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def demo(request):
#   return HttpResponse("Hello World")


def demo(request):
  return render(request,'index.html')