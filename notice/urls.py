from django.urls import path
from . import views

urlpatterns = [
    path('add-notice',views.addnotice,name="addnotice"),
    path('adding-notice',views.addingnotice,name="addnotice"),
    path('notice/<str:noticeslug>',views.shownotice,name="shownotice"),
]