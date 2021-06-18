from django.shortcuts import  redirect, render
from events.models import Event
from accounts.models import extUser
from django.contrib.auth.decorators import login_required

rolelist = ['HOD','Principal','D.G.','Moderator']
def addevent(request):
    global rolelist
    if request.user.exuser.role in rolelist:
        euser=extUser.objects.get(user__id=request.user.id)
        return render(request,'events/add_event.html',{'euser':euser})
    else:
        return redirect('/error-404')

@login_required(login_url='login')
def addingevent(request):
    global rolelist
    if request.user.exuser.role in rolelist:
        if request.method=="POST":
            title=request.POST["title"]
            slogan=request.POST["event_slogan"]
            category=request.POST["eventcat"]
            start_date=request.POST["start_date"] #.split("/")
            # start_date='-'.join(start_date)
            end_date=request.POST["end_date"] #.split("/")
            # end_date='-'.join(end_date)
            description=request.POST["eventdesc"]
            poster=request.FILES["event_poster"]
            slug='-'.join(title.split(' '))
            event=Event()
            event.title=title
            event.slug=slug
            event.slogan=slogan
            event.category=category
            event.start_date=start_date
            event.end_date=end_date
            event.descripton=description
            event.poster=poster
            event.save()
            return redirect('/add-event')
    else:
        return redirect('/error-404')
        
@login_required(login_url='login')
def showevent(request,eventslug):
    event=Event.objects.get(slug=eventslug)
    otherevents=Event.objects.exclude(slug=eventslug)
    return render(request,'events/show_event.html',{'event':event,'otherevents':otherevents})