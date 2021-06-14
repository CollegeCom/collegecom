from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=100)
    slogan=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    start_date=models.CharField(max_length=100,blank=True)
    end_date=models.CharField(max_length=100,blank=True)
    descripton=models.TextField(max_length=1000)
    poster=models.ImageField(upload_to='poster/')

    def __str__(self):
        return self.title
    
