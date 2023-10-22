from django.db import models


# # Create your models here.

class TakerAbotpage(models.Model):
    introduction=models.CharField(max_length=255)
    petexperience=models.CharField(max_length=255)
    workstatus=models.CharField(max_length=255)
    skillandqualifications=models.CharField(max_length=255)
    otherpetqualifications=models.CharField(max_length=255,null=True)





