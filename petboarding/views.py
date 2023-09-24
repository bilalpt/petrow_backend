from django.shortcuts import render
from .serilizers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView



# Create your views here.

# login and create token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

class petboard(CreateAPIView):

    # def get(self,request):
    #     user=User.objects.all()
    #     userseriliz=Userserilizers(user,many=True)
    #     return Response({'status':200,'values':userseriliz.data,'message':'success'})

    def post(self,request):
        serials=Userserilizers(data=request.data)
        if not serials.is_valid():
            return Response({'status':403,'message':'invalid values'})
        else:
            serials.save()
            return Response({'status':200,'message':'success'})




