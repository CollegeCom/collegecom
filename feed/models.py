from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Feed(models.Model):
    message=models.TextField(max_length=10000)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    date_time=models.CharField(max_length=50)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    image=models.ImageField(upload_to='feed_images/')

    def __str__(self):
        return self.posted_by+" "+self.date_time
    