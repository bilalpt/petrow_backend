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
from rest_framework.generics import CreateAPIView,DestroyAPIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

from django.views import View
from petboarding.models import User
from petboarding.serilizers import *

import json
# for the multiple image
from django.views.decorators.csrf import csrf_exempt

# user chekking
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

#list api view
from rest_framework.generics import ListAPIView






# Create your views here.

class Generatetoken(TokenObtainPairView):
    serializer_class=Petcareserilatoken


class Petcare(APIView):

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

class AboutpageRetrive(ListAPIView):
    serializer_class=TakerAboutPageserial
    def get_queryset(self):
        user_id=self.kwargs['id']
        queryset=TakerAbotpag.objects.filter(user_id=user_id)
        return queryset
    


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

            redirect_url = 'https://petrow-frondent-ceo4ey3nc-bilalpts-projects.vercel.app/PetBoards/CareLogin' + '?message=' + message + '&token' + str(token)

    else:
        message = 'Invalid activation link'
        redirect_url =  'https://petrow-frondent-ceo4ey3nc-bilalpts-projects.vercel.app/CareSignup/' + '?message=' + message
    
    
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
        Aboutget=TakerAbotpag.objects.all()
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


#taker about edit

class TakeraboutEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=TakerAboutPageserial
    lookup_field='id'
    queryset=TakerAbotpag.objects.all()


#taker service descriptions and details

class ServiceDescriptionView(APIView):
    def get(self,request):
        describdata=DescribeServicetwo.objects.all()
        serializer=ServiceDescriptionSerial(describdata,many=True)
        return Response({'sucess':200,'data':serializer.data})
    def post(self,request):
        serializer=ServiceDescriptionSerial(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'msg': 'Data saved successfully', 'data': serializer.data})
        else:
            return Response({'status':400,'message':'error'})

#service description retreve
class descriptionRetrive(ListAPIView):
    serializer_class=ServiceDescriptionSerial
    def get_queryset(self):
        user_id=self.kwargs['id']
        queryset=DescribeServicetwo.objects.filter(user_id=user_id)
        return queryset


#taker service description
class ServiceDescriptionEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=ServiceDescriptionSerial
    lookup_field='id'
    queryset=DescribeServicetwo.objects.all()


# taker with pet
class Takerwithpet(CreateAPIView):
    serializer_class=TakerwithpetSerial
    queryset=Takerwithpets.objects.all()

# taker with pet edit
class TakerwithpetEdit(RetrieveUpdateDestroyAPIView):
    serializer_class =TakerwithpetSerial
    lookup_field='id'
    queryset=Takerwithpets.objects.all()

#taker user details
            
class TakerUserInfo(RetrieveUpdateDestroyAPIView):
    serializer_class = PetcareSerilizers
    queryset = User.objects.all()



# taker profile edit

class TakerprofileEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=PetcareSerilizers
    lookup_field='id'
    queryset=User.objects.all()


#taker id proof multiple images

class Takeridproofclass(ListCreateAPIView):
    queryset = Takeridproof.objects.all()
    serializer_class = Takeridproofserial

    def create(self, request, *args, **kwargs):
        images_data = request.data.getlist('images')  # Assuming images is a list of image data
        takeridproof_serializer = self.get_serializer(data=request.data)
        if takeridproof_serializer.is_valid():
            takeridproof = takeridproof_serializer.save()
            # Save images
            for image_data in images_data:
                takeridproof.images.create(image=image_data)
            return Response(self.get_serializer(takeridproof).data, status=status.HTTP_201_CREATED)
        return Response(takeridproof_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#taker id proof with form
    
class TakeridwithformView(CreateAPIView):
    serializer_class=TakerFormidproofserial 
    queryset=TakerwithIdform.objects.all()


#taker request page image pass

class TakerIdRetreve(ListAPIView):
    serializer_class=TakerFormidproofserial
    def get_queryset(self):
        user_id=self.kwargs['id']
        queryset=TakerwithIdform.objects.filter(user_id=user_id)
        return queryset

#taker  id proof edit 
class TakeridproofEdit(RetrieveUpdateDestroyAPIView):
    serializer_class=TakerFormidproofserial
    lookup_field='id'
    queryset=TakerwithIdform.objects.all()


#taker id proofs listed   
class Takeridproofallretreave(ListAPIView):
    serializer_class=TakerFormidproofserial
    queryset=TakerwithIdform.objects.all()

# taker request edit 
class Takerrequestupdate(RetrieveUpdateDestroyAPIView):
    serializer_class= PetcareSerilizers  
    lookup_field='id'
    queryset=User.objects.all()

# petwith image listing in accept reject page in admin side

class Petwithimagelist(ListAPIView):
    serializer_class=TakerwithpetSerial
    def get_queryset(self):
        user_id=self.kwargs['id']
        queryset=Takerwithpets.objects.filter(user_id=user_id)
        return queryset

# taker reject time delete section
class Takeridformdelete(DestroyAPIView):
    queryset = TakerwithIdform.objects.all()
    serializer_class = TakerFormidproofserial
    lookup_url_kwarg = 'id'  

# Home showing Taker users

class Takerusershow(ListAPIView):
    serializer_class=TakerCompainedserializers
    def list(self, request, *args, **kwargs):
        accepteduser=[]
        aboutuser=[]
        descriptions=[]
        withpet=[]

        taker_queryset = TakerwithIdform.objects.filter(Takeraccept=True)
        for i in taker_queryset:
            accepteduser.append(i.user)

        accepteduser=accepteduser[-3:]
    

        for j in accepteduser:
            removeduplicate=set()
            descriptiondata=DescribeServicetwo.objects.filter(user=j)
            for description in descriptiondata:
                if description.user.id and description.user.id not in removeduplicate:
                    removeduplicate.add(description.user.id)
                    descriptions.append(description)

            abotpage=TakerAbotpag.objects.filter(user=j)
            duplicate=set()
            for z in abotpage:
                if z.user.id and z.user.id not in duplicate:
                    duplicate.add(z.user.id)
                    aboutuser.append(z)
                    

            withpets=Takerwithpets.objects.filter(user=j)
            setduplicate=set()
            for pets in withpets:
                if pets.user.id and pets.user.id not in setduplicate:
                    setduplicate.add(pets.user.id)
                    withpet.append(pets)


        try:
            serializers=self.get_serializer({
                'takerformidserialdatas':taker_queryset,
                'ServiceDescriptiondata':descriptions,
                'Takeraboutdata':aboutuser,
                'Takerwithpetdata':withpet,

            })
            return Response(serializers.data)
        except Exception as e:
            print(f"Error in showtakerdetails view: {e}")
            return Response({"error": "Internal Server Error"})



