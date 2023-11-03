from rest_framework import serializers
from  petboarding.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class PetcareSerilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','phone','roles']


class TakerAboutPageserial(serializers.ModelSerializer):
    class Meta:
        model=TakerAbotpage
        fields=['id','introduction','petexperience','workstatus','skillandqualifications','otherpetqualifications']



class ServiceDescriptionSerial(serializers.ModelSerializer):
    class Meta:
        model=DescribeService
        fields=['id','servicename','petcount','acceptingpet','acceptingpetsize','howmanywalk','apartmentorhome','transportemergencies','sleepinglocation','price','location','pincode']
        

class TakerwithpetSerial(serializers.ModelSerializer):
    class Meta:
        model=Takerwithpet
        fields=['id','image','uploaded_at']

class Takeridproofserial(serializers.ModelSerializer):
    class Meta:
        model = Takeridproof
        fields = '__all__'

class TakerFormidproofserial(serializers.ModelSerializer):
    class Meta:
        model = TakerwithIdform
        fields='__all__'



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



