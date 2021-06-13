from django.shortcuts import render

# Create your views here.
def addfeedback(request):
    return render(request,'feedback/addfeedback.html')

def addcomplaint(request):
    return render(request,'feedback/addcomplaint.html')


def complaints(request):
    return render(request,'feedback/complaint-list.html')