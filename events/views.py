from django.shortcuts import  redirect, render
from events.models import Event
from django.http import HttpResponse
def addevent(request):
    return render(request,'events/add_event.html')

def addingevent(request):
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
        event=Event()
        event.title=title
        event.slogan=slogan
        event.category=category
        event.start_date=start_date
        event.end_date=end_date
        event.descripton=description
        event.poster=poster
        event.save()

        return redirect('/add-event')

        