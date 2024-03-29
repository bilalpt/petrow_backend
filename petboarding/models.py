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
    roles=models.CharField(max_length=20,choices=USER_ROLES,default='admin')
    is_active = models.BooleanField(default=False)
    profileimage =models.ImageField(upload_to='userprofileimage/',null=True)
    date_and_time = models.DateField(auto_now_add=True,null=True)




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # branch rename 

class BoardingForm(models.Model):
    pettype=models.CharField(max_length=12)
    nuberofpetboarded=models.CharField(max_length=20)
    petbreed=models.CharField(max_length=200)
    petsize=models.CharField(max_length=200)
    additionalinfo=models.CharField(max_length=240)
    startdate=models.DateField()
    enddate=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pincode=models.CharField(max_length=10,null=True)




