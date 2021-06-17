from django.db import models

# Create your models here.
class Notice(models.Model):
    title=models.CharField(max_length=100)
    slogan=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    date=models.CharField(max_length=100,blank=True)
    descripton=models.TextField(max_length=1000)
    file=models.FileField(upload_to='notice/')

    def __str__(self):
        return self.title
    
