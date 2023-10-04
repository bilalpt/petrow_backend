from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    USER_ROLES=(
        ('boarduser','Boarduser'),
        ('taker','Taker'),
        ('admin','Admin'),
    )


    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=14)
    # profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    password=models.CharField(max_length=200)
    roles=models.CharField(max_length=20,choices=USER_ROLES,default='boarduser')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    




