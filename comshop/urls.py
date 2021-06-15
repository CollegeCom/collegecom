from django.urls import path
from . import views

urlpatterns = [
    path('shop',views.shop,name="shop"),
    path('add-product',views.addproduct,name="addproduct"),
]
