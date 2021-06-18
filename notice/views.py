from django.shortcuts import  redirect, render
from notice.models import Notice
from django.http import HttpResponse
from accounts.models import extUser
def addnotice(request):
    euser=extUser.objects.get(user__id=request.user.id)
    return render(request,'notices/add_notice.html',{'euser':euser})

def addingnotice(request):
    if request.method=="POST":
        title=request.POST["title"]
        slogan=request.POST["notice_slogan"]
        category=request.POST["noticecat"]
        date=request.POST["date"]
        description=request.POST["noticedesc"]
        poster=request.FILES["notice_file"]
        notice=Notice()
        notice.title=title
        notice.slogan=slogan
        notice.category=category
        notice.date=date
        notice.descripton=description
        notice.file=poster
        notice.save()
        return redirect('/add-notice' ,{'msgs':1})

def shownotice(request,noticeslug):
    event=Notice.objects.get(slug=noticeslug)
    othernotices=Notice.objects.exclude(slug=noticeslug)
    return render(request,'events/show_event.html',{'event':event,'othernotices':othernotices})

        