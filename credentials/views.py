from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
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
                return render(request,'/')
        else:
            messages.info(request,'password not match')    
            return redirect('register')   
    return render(request,'register.html')