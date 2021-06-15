from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from events.models import Event
from accounts.models import extUser

@login_required(login_url='login')
def home(request):
    events=Event.objects.all()
    user=extUser.objects.get(user__id=request.user.id)
    params={"events":events,"euser":user}
    return render(request,'dashboard.html',params)
