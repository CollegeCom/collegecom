from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.shortcuts import redirect
from accounts.models import extUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from feedback.models import Complaint,Feedback
import os

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'accounts/login.html')

@login_required(login_url='login')
def profile(request):
    exuser = extUser.objects.get(user__id=request.user.id)
    parmas = {'euser':exuser}
    return render(request,'accounts/profile.html',parmas)

def reg_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        username = email.split('@')[0]

        username.lower()
        email.lower()
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            success=2
            return HttpResponse(success)
        elif User.objects.filter(email=email).exists():
            success=2
            return HttpResponse(success)
        else:
            if (email.split('@')[1]!='indoreinstitute.com'):
                success=3
                return HttpResponse(success)
            else:
                newuser = User.objects.create_user(username,email,password)
                newuser.first_name=first_name
                newuser.last_name=last_name
                newuser.is_active=True
                newuser.save()
                extuser = extUser(user=newuser)
                extuser.save()
                success=1
                return HttpResponse(success)

def loginuser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username,password=password)
            if user is not None:
                authlogin(request,user)
                success=1
                return HttpResponse(success)
            else:
                success=2
                return HttpResponse(success)
        else:
            success=3
            return HttpResponse(success)
    else:
        return redirect('/')
    

def log_out(request):
    logout(request)
    return redirect('login')

def updateprofile(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        institution=request.POST['institution']
        cemail=request.POST['cemail']
        linkedin=request.POST['linkedin']
        enroll=request.POST['enroll']
        sem=request.POST['sem']
        city=request.POST['location']
        user=User.objects.get(id=request.user.id)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        up=extUser.objects.get(user__id=request.user.id)
        try:
            profileimg=request.FILES['profileimg']
            oldimage=up.profileimg.path
            os.remove(oldimage)
            up.profileimg=profileimg
        except :
            pass
        up.institution=institution
        up.cemail=cemail
        up.enroll=enroll
        up.linkedin=linkedin
        up.sem=sem
        up.city=city
        up.save()
        success=1
        return HttpResponse(success)


def profile_overview(request):
    comp=Complaint.objects.filter(postedby=request.user.username)
    feedback=Feedback.objects.filter(postedby=request.user.username)
    euser=extUser.objects.get(user__id=request.user.id)
    params={'comp':comp,'feedback':feedback,'euser':euser}
    return render(request,'accounts/profile-overview.html',params)

def contacts(request):
    euser=extUser.objects.exclude(user__id=request.user.id)
    cuser=extUser.objects.get(user__id=request.user.id)
    return render(request,'accounts/contacts.html',{'contacts':euser,'euser':cuser})