from django.urls import path
from . import views

urlpatterns = [
    path('add-event',views.addevent,name="addevent"),
    path('adding-event',views.addingevent,name="addevent"),
    path('event/<str:eventslug>',views.showevent,name='showevent'),
]