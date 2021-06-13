from django.db import models

# Create your models here.
class Complaint(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    postedby=models.CharField(max_length=50)
    userenroll=models.CharField(max_length=50)
    useremail=models.CharField(max_length=80)
    issuecat=models.CharField(max_length=20)
    issuedesc=models.TextField()
    status=models.IntegerField(default=0,blank=True)

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    event=models.CharField(max_length=100)
    postedby=models.CharField(max_length=50)
    userenroll=models.CharField(max_length=50)
    useremail=models.CharField(max_length=80)
    feedback=models.TextField()