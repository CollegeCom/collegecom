from django.shortcuts import  redirect, render
from notice.models import Notice
from accounts.models import extUser
from django.contrib.auth.decorators import login_required
rolelist = ['HOD','Principal','D.G.','Moderator']
@login_required(login_url='login')
def addnotice(request):
    global rolelist
    if request.user.exuser.role in rolelist:
        euser=extUser.objects.get(user__id=request.user.id)
        return render(request,'notices/add_notice.html',{'euser':euser})
    else:
        return redirect('/error-404')

@login_required(login_url='login')
def addingnotice(request):
    global rolelist
    if request.user.exuser.role in rolelist:
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
    else:
        return redirect('/error-404')

@login_required(login_url='login')
def shownotice(request,noticeslug):
    event=Notice.objects.get(slug=noticeslug)
    othernotices=Notice.objects.exclude(slug=noticeslug)
    return render(request,'events/show_event.html',{'event':event,'othernotices':othernotices})

        