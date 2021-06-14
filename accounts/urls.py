from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('profile',views.profile,name='profile'),
    path('login-user',views.loginuser,name="loginuser"),
    path('register-user',views.reg_user,name="reg_user"),
    path('logout',views.log_out,name="log_out"),
    path('update-profile',views.updateprofile,name="updateprofile"),
    # path('register-user',views.registeruser,name="registeruser"),
]
