from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from events.models import Event
from notice.models import Notice
from accounts.models import extUser
from feed.models import Feed

@login_required(login_url='login')
def home(request):
    feed=Feed.objects.order_by('-id')
    events=Event.objects.all()
    notices=Notice.objects.all()
    user=extUser.objects.get(user__id=request.user.id)
    params={"euser":user,'feed':feed,'events':events[::-1][:3],'notices':notices[::-1][:3]}
    return render(request,'dashboard.html',params)
