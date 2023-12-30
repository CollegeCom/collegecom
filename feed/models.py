from accounts.models import extUser
from django.db import models

class Feed(models.Model):
    published_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    message=models.TextField()
    posted_by=models.ForeignKey(extUser,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    image=models.ImageField(upload_to='feed_images/')

    def __str__(self):
        return self.posted_by.user.username+" "+self.date_time
    
class Comment(models.Model):
    published_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    comment=models.TextField()
    posted_by=models.ForeignKey(extUser,on_delete=models.CASCADE)
    feed=models.ForeignKey(Feed,related_name="feeds",on_delete=models.CASCADE)