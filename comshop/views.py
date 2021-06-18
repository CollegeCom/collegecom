from django.db.models.query_utils import Q
from accounts.models import extUser
from comshop.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import date
from accounts.models import extUser
# Create your views here.
def shop(request):
    products=Product.objects.all()
    euser=extUser.objects.get(user__id=request.user.id)
    params={'products':products,'euser':euser}
    return render(request,'comshop/shophome.html',params)

def addproduct(request):
    if request.method=="POST":
        title=request.POST['title']
        category='College'
        postedby=request.user.username
        description=request.POST['description']
        postdate=date.today()
        price=request.POST['price']
        productimg=request.FILES['productimage']
        ap=Product()
        ap.title=title
        ap.category=category
        ap.postedby=postedby
        ap.description=description
        ap.postdate=postdate
        ap.price=price
        ap.productimg=productimg
        ap.save()
        return redirect('shop')

def shopsearch(request):
    if request.method=="GET":
        search=request.GET['search']
        products=Product.objects.filter(Q(category__icontains=search) | Q(title__icontains=search))
        print(products)
        return render(request,'comshop/shophome.html',{'products':products})
