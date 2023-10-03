from django.shortcuts import render
from .serilizers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import status


from rest_framework.decorators import api_view
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken










# Create your views here.

# login and create token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

    

class petboard(APIView):

    def get(self,request):
        user=User.objects.all()
        userseriliz=Userserilizers(user,many=True)
        return Response({'status':200,'values':userseriliz.data,'message':'success'})

    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        print('daxo')
        serializer=Userserilizers(data=request.data)
        if  serializer.is_valid():
            user=serializer.save()
            user.role = 'professional'
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
        redirect_url =  'http://localhost:5173/login/' + '?message=' + message + '?token' + token
    else:
        message = 'Invalid activation link'
        redirect_url = 'http://localhost:5173/signup/' + '?message=' + message
    
    
    return HttpResponseRedirect(redirect_url)  


class googlesignup(APIView):

    # def get(self,request):

    #     one=User.objects.all()
    #     print(one)

    #     serializ=Userserilizers(one,many=True)
    #     return Response({'status':200,'values':serializ.data,'message':'success'})
        


    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')


        if not User.objects.filter(email=email).exists():
            serializer = Userserilizers(data = request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.role = 'homeowner'
                user.is_active = True
                user.is_google = True
                user.set_password(password)
                user.save()

        
        user = authenticate(request, email=email, password=password)
        if user is not None:

            token=create_jwt_pair_tokens(user)

            response_data = {
                'status' : 'success',
                'token' : token,
                'msg' : 'Account has been registered succesfully',
            }

            return Response (data=response_data, status = status.HTTP_201_CREATED)
        else:
            return Response (data={'status' : '400' , 'msg' : 'Login failed'})
        


def create_jwt_pair_tokens(user):
    
    refresh = RefreshToken.for_user(user)

    refresh['email'] = user.email
    refresh['id'] = user.id
    refresh['username'] = user.username
    refresh['role'] = user.role
    refresh['is_active'] = user.is_active

   
    access_token = str(refresh.access_token) # type: ignore
    refresh_token = str(refresh)

    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }




