from django.db import models

# Create your models here.
class NfoMOdels(models.Model):
    email=models.CharField(max_length=50)
    psw=models.CharField(max_length=50)
    psw_repeat=models.CharField(max_length=50)

class VoterDetails(models.Model):
    yname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    bewith = models.CharField(max_length=50)
