  
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class extUser(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=255,blank=True,null=True)
    enroll = models.CharField(max_length=255,blank=True,null=True)
    sem = models.IntegerField(default=1)
    branch = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    institution = models.CharField(max_length=255,blank=True,null=True)



    def __str__(self):
        return self.user.username
