from django.db import models
from petboarding.models import *


# # Create your models here.

#taker about page

class TakerAbotpage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    introduction=models.CharField(max_length=255)
    petexperience=models.CharField(max_length=255)
    workstatus=models.CharField(max_length=255)
    skillandqualifications=models.CharField(max_length=255)
    otherpetqualifications=models.CharField(max_length=255,null=True)


#taker description
 
class DescribeService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    servicename=models.CharField(max_length=255)
    petcount=models.CharField(max_length=20)
    acceptingpet=models.CharField(max_length=12)
    acceptingpetsize=models.CharField(max_length=20)
    howmanywalk=models.CharField(max_length=8)
    apartmentorhome=models.CharField(max_length=20)
    transportemergencies=models.CharField(max_length=10)
    sleepinglocation=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    pincode=models.IntegerField()

# taker with pet images    

class Takerwithpet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    

class Takeridproof(models.Model):
    proofimage=models.ImageField(upload_to='uploads/')

