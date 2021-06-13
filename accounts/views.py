from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.shortcuts import redirect
from accounts.models import extUser
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def profile(request):
    exuser = extUser.objects.get(user__id=request.user.id)
    parmas = {'euser':exuser}
    return render(request,'accounts/profile.html',parmas)

def loginuser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            us = User.objects.get(username=username)
            user = authenticate(username=username,password=password)
            if user is not None:
                authlogin(request,user)
                return redirect('/')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('/')

def log_out(request):
    logout(request)
    return redirect('login')