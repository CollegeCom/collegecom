from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from events.models import Event

@login_required(login_url='login')
def home(request):
    events=Event.objects.all()
    params={"events":events}
    return render(request,'dashboard.html',params)
