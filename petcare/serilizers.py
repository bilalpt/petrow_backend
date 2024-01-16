from rest_framework import serializers
from  petboarding.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from petcare.models import *

class PetcareSerilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','phone','roles','profileimage']

#taker about page serial
class TakerAboutPageserial(serializers.ModelSerializer):
    class Meta:
        model=TakerAbotpag
        fields=['id','introduction','petexperience','workstatus','skillandqualifications','otherpetqualifications','user']


#taker description serial
class ServiceDescriptionSerial(serializers.ModelSerializer):
    class Meta:
        model=DescribeServicetwo
        fields=['id','servicename','petcount','acceptingpet','acceptingpetsize','howmanywalk','apartmentorhome','transportemergencies','sleepinglocation','price','location','pincode','user']
        
#taker with pet serial
class TakerwithpetSerial(serializers.ModelSerializer):
    class Meta:
        model=Takerwithpets
        fields=['id','image','uploaded_at','user']

class Takeridproofserial(serializers.ModelSerializer):
    class Meta:
        model = Takeridproof
        fields = ['id','proofimage']

class TakerFormidproofserial(serializers.ModelSerializer):
    class Meta:
        model = TakerwithIdform
        fields=['id','adharimg','otheridimg','user','Takeraccept']

    


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



