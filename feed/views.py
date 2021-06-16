from accounts.models import extUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Comment, Feed
from datetime import date
import time
# Create your views here.
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
        return redirect('home')

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
        return redirect('home')


