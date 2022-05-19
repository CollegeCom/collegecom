from django.urls import path
from . import views

urlpatterns = [
    path('add-feedback/',views.addfeedback,name="addfeedback"),
    path('add-complaint/',views.addcomplaint,name="addcomplaint"),
    path('complaint/s',views.complaints,name="complaints"),
    path('adding-complaint',views.addingcomplaint,name="addingcomplaint"),
    path('adding-feedback',views.addingfeedback,name="addingfeedback"),
    path('complaint-status',views.complaint_status,name="complaint_status"),
    
]
