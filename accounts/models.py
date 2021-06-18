  
from django.db import models
from django.contrib.auth.models import User
ROLES = [
    ('Student', 'Student'),
    ('HOD', 'Head of Department'),
    ('Faculty', 'Faculty'),
    ('Students Dept.', 'Students Department'),
    ('Accounts Dept.', 'Accounts Department'),
    ('D.G.', 'Director General'),
    ('Principal', 'Principal'),
    ('Moderator', 'Moderator'),
]


# Create your models here.
class extUser(models.Model):  
    user = models.OneToOneField(User,related_name='exuser',on_delete=models.CASCADE)
    city = models.CharField(max_length=255,blank=True,null=True)
    enroll = models.CharField(max_length=255,blank=True,null=True)
    sem = models.CharField(max_length=50,default="First",blank=True)
    branch = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    linkedin=models.CharField(max_length=100,blank=True)
    cemail=models.CharField(max_length=60,blank=True)
    role=models.CharField(max_length=100,choices=ROLES,default='Student')
    department=models.CharField(max_length=100,default="IIST",blank=True)
    institution = models.CharField(max_length=255,blank=True,null=True)
    vbadge = models.BooleanField(default=False)
    profileimg=models.ImageField(upload_to='profile_images/',default="profile_images/user.png")



    def __str__(self):
        return self.user.username
