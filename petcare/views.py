from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serilizers import Petcareserilatoken
from rest_framework.views import APIView
from .serilizers import *
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import HttpResponseRedirect
from decouple import config
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from django.views import View
from petboarding.models import User

import json





# Create your views here.

class Generatetoken(TokenObtainPairView):
    serializer_class=Petcareserilatoken


class Petcare(APIView):

    # def get(self,request):

    #     user=User.objects.all()
    #     userserial=Petcareserilatoken(user,many=True)
    #     return Response({'success'})
                




    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        print('baxter')

        serializer=PetcareSerilizers(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.roles='taker'
            user.set_password(password)
            user.save()




            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('account_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'cite': current_site.domain

            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            response_data = {
                'status': 'success',
                'msg': 'A verification link sent to your registered email address',
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            print('Serializer errors are:', serializer.errors)
            return Response({'status': 'error', 'msg': serializer.errors})
        


#gmail activation 
@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
      
        message = "Congrats, You have been succesfully registered"
        token=create_jwt_pair_tokens_taker(user)
        # Baseurl=config('Baseurl')
        if user.roles=='taker':

            redirect_url = 'http://localhost:5173/PetBoards/CareLogin' + '?message=' + message + '&token' + str(token)
       

    else:
        message = 'Invalid activation link'
        redirect_url =  'http://localhost:5173/CareSignup/' + '?message=' + message
    
    
    return HttpResponseRedirect(redirect_url)





def create_jwt_pair_tokens_taker(taker):
    
    refresh = RefreshToken.for_user(taker)

    refresh['email'] = taker.email
    refresh['id'] = taker.id
    refresh['username'] = taker.username
    refresh['role'] = taker.role
    refresh['is_active'] = taker.is_active
    refresh['roles'] = taker.roles

   
    access_token = str(refresh.access_token) # type: ignore
    refresh_token = str(refresh)

    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


#taker about form backend

class TakerAboutView(APIView):
    
    def get(self,request):
        Aboutget=TakerAbotpage.objects.all()

        serializer=TakerAboutPageserial(Aboutget,many=True)
        return Response({'status':200,'values':serializer.data,'message':'sucess'})
        
    def post(self, request):

        serializer = TakerAboutPageserial(data=request.data)
        if serializer.is_valid():
            print(request.data)

            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status': 400, 'message': 'error', 'errors': serializer.errors})


# class TakerAboutView(CreateAPIView):
#     serializer_class=TakerAboutPageserial
#     queryset=TakerAbotpage.objects.all()


#taker service descriptions and details

class ServiceDescriptionView(APIView):
    
    #get method
    def get(self,request):
        describdata=DescribeService.objects.all()
        serializer=ServiceDescriptionSerial(describdata,many=True)
        return Response({'sucess':200,'data':serializer.data})
    
    def post(self,request):

        serializer=ServiceDescriptionSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status':400,'message':'error'})

#taker service description

class ServiceDescriptionEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=ServiceDescriptionSerial
    lookup_field='id'
    queryset=DescribeService.objects.all()


# taker with pet

class Takerwithpet(CreateAPIView):
    serializer_class=TakerwithpetSerial
    queryset=Takerwithpet.objects.all()
    

#taker user details
            
class TakerUserInfo(RetrieveUpdateDestroyAPIView):
    serializer_class = PetcareSerilizers
    queryset = User.objects.all()


# taker profile edit

class TakerprofileEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=PetcareSerilizers
    lookup_field='id'
    queryset=User.objects.all()



class Takeridproof(CreateAPIView):
    queryset = Takeridproof.objects.all()
    serializer_class = Takeridproofserial

    def create(self, request, *args, **kwargs):
        images = request.data.pop('images', [])
        pet = Takeridproof.objects.create(**request.data)
        for image in images:
            pet.images.create(image=image)
        return Response(self.get_serializer(pet).data, status=status.HTTP_201_CREATED)

    

