from rest_framework import serializers
from  .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class Userserilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','phone','roles']

                
    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = super().create(validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user

class forgotpasswordserial(serializers.ModelSerializer):
        class Meta:
            model=User
            feilds=['username','email','password','phone','roles']




class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id']=user.id   
        token['username'] = user.username
        token['email'] = user.email
        token['is_admin'] = user.is_superuser

        return token        