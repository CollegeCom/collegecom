from accounts.models import extUser
from django.db import models
# Create your models here.
class Feed(models.Model):
    message=models.TextField()
    posted_by=models.ForeignKey(extUser,on_delete=models.CASCADE)
    date_time=models.CharField(max_length=50)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    image=models.ImageField(upload_to='feed_images/')

    def __str__(self):
        return self.posted_by.user.username+" "+self.date_time
    
class Comment(models.Model):
    comment=models.TextField()
    posted_by=models.ForeignKey(extUser,on_delete=models.CASCADE)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    feed=models.ForeignKey(Feed,related_name="feeds",on_delete=models.CASCADE)