from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)

class Emp1(models.Model):
    name1=models.CharField(max_length=50)
    dob=models.DateField()

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='media')

class Gallery(models.Model):
    gimage = models.ImageField(upload_to='gallery')
    progallery=models.ForeignKey(Hotel,on_delete=models.CASCADE, related_name='info')