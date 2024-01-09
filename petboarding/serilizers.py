from rest_framework import serializers
from  .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from petcare.models import *

from petcare.serilizers import *



class Userserilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password','phone','roles','profileimage','is_active','date_and_time']


class forgotpasswordserial(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=['username','email','password','phone','roles']


class Boardformserial(serializers.ModelSerializer):
     class Meta:
          model = BoardingForm
          fields= ['id','pettype','nuberofpetboarded','petbreed','petsize','additionalinfo','startdate','enddate','pincode','user']

class TakerFormidproofserialPetcare(serializers.ModelSerializer):
    class Meta:
        model = TakerwithIdform
        fields=['id','adharimg','otheridimg','user','Takeraccept']


class ServiceDescriptionSerial(serializers.ModelSerializer):
    class Meta:
        model=DescribeServicetwo
        fields=['id','servicename','petcount','acceptingpet','acceptingpetsize','howmanywalk','apartmentorhome','transportemergencies','sleepinglocation','price','location','pincode','user']        

class Compainedserializers(serializers.Serializer):
    takerformidserialdatas = TakerFormidproofserialPetcare(many=True)
    boardingformdata = Boardformserial(many=True)
    ServiceDescriptiondata=ServiceDescriptionSerial(many=True)




class inviteusers(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields=['id','sender','receiver','status','request']




class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id']=user.id   
        token['username'] = user.username
        token['email'] = user.email
        token['is_admin'] = user.is_superuser
        token['roles'] = user.roles

        return token        