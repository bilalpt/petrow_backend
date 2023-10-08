from rest_framework import serializers
from petboarding.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class adminserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        feilds=['username','email','password','phone','roles']





class AdmintokenpairSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['id']=user.id
        token['username']=user.username
        token['email']=user.email
        token['password']=user.password
        token['is_admin']=user.is_superuser

        return token


    