from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('profile',views.profile,name='profile'),
]
