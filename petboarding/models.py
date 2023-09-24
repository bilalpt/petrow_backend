from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=14,unique=True)
    # profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    password=models.CharField(max_length=200)

    REQUIRED_FIELDS = ['email']




