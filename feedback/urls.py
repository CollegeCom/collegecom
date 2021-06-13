from django.urls import path
from . import views

urlpatterns = [
    path('add-feedback',views.addfeedback,name="addfeedback"),
    path('add-complaint',views.addcomplaint,name="addcomplaint"),
]
