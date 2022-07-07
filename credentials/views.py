from django.contrib import messages,auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(password)
        print(username)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"inalid credentials")
            return redirect('login')    
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['conf_password']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username  Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email  Taken')
                return redirect('register')    
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print('user created')
                return redirect(request,'home')
        else:
            messages.info(request,'password not match')    
            return redirect('register')   
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')