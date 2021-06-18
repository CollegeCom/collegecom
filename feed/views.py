from accounts.models import extUser
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Comment, Feed
from datetime import date
from django.contrib.auth.decorators import login_required
import time
# Create your views here.

@login_required(login_url='login')
def addpost(request):
    if request.method=="POST":
        message=request.POST['message']
        postedby=extUser.objects.get(user__id=request.user.id)
        date_time=date.today()
        af=Feed()
        af.message=message
        af.posted_by=postedby
        af.date_time=date_time
        try:
            image=request.FILES['postimage']
            af.image=image
        except:
            pass
        af.save()
        success=str(af.image)
        return HttpResponse(success)
        
@login_required(login_url='login')
def addcomment(request):
    if request.method=="POST":
        comment=request.POST['comment']
        feedid=request.POST['feedid']
        postedby=extUser.objects.get(user__id=request.user.id)
        cdate=date.today()
        ctime=time.localtime()
        feed=Feed.objects.get(id=feedid)
        cm=Comment()
        cm.comment=comment
        cm.posted_by=postedby
        cm.date=cdate
        cm.time=ctime
        cm.feed=feed
        cm.save()
        feed.comments+=1
        feed.save()
        return redirect('home')


