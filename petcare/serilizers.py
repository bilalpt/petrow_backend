from rest_framework import serializers
from  petboarding.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PetcareSerilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','phone','roles']



class Petcareserilatoken(TokenObtainPairSerializer):
    def get_token(cls,user):
        token=super().create(user)
        token['id']=user.id
        token['username']=user.username
        token['email']=user.email
        token['is_admin']=user.is_superuser
        return token



