from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request,'dashboard.html')
