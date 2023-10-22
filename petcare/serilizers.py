from rest_framework import serializers
from  petboarding.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class PetcareSerilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','phone','roles']

class TakerAboutPageserial(serializers.ModelSerializer):
    class Meta:
        model=TakerAbotpage
        fields=['id','introduction','petexperience','workstatus','skillandqualifications','otherpetqualifications']


class ServiceDescriptionSerial(serializers.ModelSerializer):
    class Meta:
        model=DescribeService
        fields=['id','servicename','petcount','acceptingpet','acceptingpetsize','howmanywalk','apartmentorhome','transportemergencies','sleepinglocation','price','location','pincode']


class Petcareserilatoken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id']=user.id
        token['username']=user.username
        token['email']=user.email
        token['is_admin']=user.is_superuser
        token['roles']=user.roles
        return token



