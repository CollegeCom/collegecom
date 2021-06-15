from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    postedby=models.CharField(max_length=50,blank=True)
    description=models.TextField()
    productimg=models.ImageField(upload_to='products/')
    postdate=models.CharField(max_length=50,blank=True)
    price=models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title
    