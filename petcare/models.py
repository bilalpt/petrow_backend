from django.db import models


# # Create your models here.

class TakerAbotpage(models.Model):
    indroduction=models.CharField(max_length=255)
    petexperience=models.CharField(max_length=255)
    enjoyment_or=models.CharField(max_length=255)
    skillandqualification=models.CharField(max_length=255)




