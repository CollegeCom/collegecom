from django.urls import path
from . import views
urlpatterns = [
   path('add-post',views.addpost,name="addpost"),
   path('add-comment',views.addcomment,name="addcomment"),
]
