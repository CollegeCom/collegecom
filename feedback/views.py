from django.http.response import HttpResponse
import feedback
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from accounts.models import extUser
from feedback.models import Complaint, Feedback

# Create your views here.
def addfeedback(request):
    feedbacks = Feedback.objects.all()
    params = {'feedbacks':feedbacks}
    return render(request,'feedback/addfeedback.html',params)

def addcomplaint(request):
    return render(request,'feedback/addcomplaint.html')


def complaints(request):
    complaints = Complaint.objects.filter(status=1)
    params = {'complaints':complaints}

    return render(request,'feedback/complaint-list.html',params)

def addingcomplaint(request):
    if request.method=="POST":
        name=request.POST['name']
        title=request.POST['issue']
        issuecat=request.POST['issuecat']
        issuedesc=request.POST['issuedesc']
        postedby=request.user.username
        euser=extUser.objects.get(user__id=request.user.id)
        userenroll=euser.enroll
        useremail=request.user.email
        com=Complaint()
        com.name=name
        com.title=title
        com.issuecat=issuecat
        com.issuedesc=issuedesc
        com.userenroll=userenroll
        com.useremail=useremail
        com.postedby=postedby
        com.save()
        return redirect('/')
    
def addingfeedback(request):
    if request.method=="POST":
        name=request.POST['name']
        event=request.POST['event']
        feedback=request.POST['feedback']
        postedby=request.user.username
        euser=extUser.objects.get(user__id=request.user.id)
        userenroll=euser.enroll
        useremail=request.user.email
        fb=Feedback()
        fb.name=name
        fb.event=event
        fb.feedback=feedback
        fb.userenroll=userenroll
        fb.useremail=useremail
        fb.postedby=postedby
        fb.save()
        return redirect('/')

def complaint_status(request):
    if request.method=="POST":
        comid=request.POST['comid']
        status=int(request.POST['status'])
        if Complaint.objects.filter(id=comid).exists():
            coms=Complaint.objects.get(id=comid)
            if status==1:
                coms.status=1
                coms.save()
                success=1
                return HttpResponse(success)
            else:
                success=2
                return HttpResponse(success)

            
