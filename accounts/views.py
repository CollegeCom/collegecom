import os
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.shortcuts import redirect
from accounts.models import extUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from feedback.models import Complaint,Feedback
from accounts.services import remove_old_image

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
        username = username.split('@')[0]
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
    
@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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
            remove_old_image(oldimage)
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

@login_required(login_url='login')
def profile_overview(request):
    comp=Complaint.objects.filter(postedby=request.user.username)
    feedback=Feedback.objects.filter(postedby=request.user.username)
    euser=extUser.objects.get(user__id=request.user.id)
    params={'comp':comp,'feedback':feedback,'euser':euser}
    return render(request,'accounts/profile-overview.html',params)

@login_required(login_url='login')
def contacts(request):
    euser=extUser.objects.exclude(user__id=request.user.id)
    cuser=extUser.objects.get(user__id=request.user.id)
    return render(request,'accounts/contacts.html',{'contacts':euser,'euser':cuser})

@login_required(login_url='login')
def search(request):
    if request.method=="GET":
        search=request.GET['search']
        s=search.split(' ')
        if len(s)>1:
            s1,s2=s[0],s[1]
        else:
            s1,s2=search,search
        print(s1,s2)
        users=extUser.objects.filter(Q(user__first_name__icontains=search) | Q(role__icontains=search) | Q(department__icontains=search) | Q(user__last_name__icontains=search) | Q(user__first_name__icontains=s1) | Q(user__last_name__icontains=s2) | Q(user__first_name__icontains=s2) | Q(user__last_name__icontains=s1) | Q(enroll__icontains=search))
        return render(request,'accounts/contacts.html',{'contacts':users})