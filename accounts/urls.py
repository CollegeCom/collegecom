from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('profile',views.profile,name='profile'),
    path('login-user',views.loginuser,name="loginuser"),
    path('logout',views.log_out,name="log_out"),
    # path('register-user',views.registeruser,name="registeruser"),
]
