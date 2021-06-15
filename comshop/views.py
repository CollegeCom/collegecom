from comshop.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import date
# Create your views here.
def shop(request):
    products=Product.objects.all()
    params={'products':products}
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

