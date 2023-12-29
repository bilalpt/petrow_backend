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
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.filters import SearchFilter

# from decouple import config



# Create your views here.

# login and create token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

    
#data add and send mail 

class petboard(APIView):

    def get(self,request):
        user=User.objects.all()
        userseriliz=Userserilizers(user,many=True)
        return Response({'status':200,'values':userseriliz.data,'message':'success'})

    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        # print('daxo')
        serializer=Userserilizers(data=request.data)
        if  serializer.is_valid():
            user=serializer.save()
            user.roles = 'boarduser'
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
        
        
# gmail activation 

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
        token = create_jwt_pair_tokens_board(user)
        if user.roles=='boarduser':

            redirect_url = 'http://localhost:5173/PetBoards/BoardLogin' + '?message=' + message + '&token' + str(token)
        else:
            redirect_url = 'http://localhost:5173/PetBoards/CareLogin' + '?message=' + message + '&token' + str(token)


    else:
        message = 'Invalid activation link'
        redirect_url = 'http://localhost:5173/PetBoards/signup/' + '?message=' + message
    
    
    return HttpResponseRedirect(redirect_url)

#generate signup token

def create_jwt_pair_tokens_board(boarduser):
    
    refresh = RefreshToken.for_user(boarduser)

    refresh['email'] = boarduser.email
    refresh['id'] = boarduser.id
    refresh['username'] = boarduser.username
    # refresh['roles'] = boarduser.roles
    refresh['is_active'] = boarduser.is_active

   
    access_token = str(refresh.access_token) # type: ignore
    refresh_token = str(refresh)

    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

#google signup

class googlesignup(APIView):
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

            token=create_jwt_pair_tokens_board(user)

            response_data = {
                'status' : 'success',
                'token' : token,
                'msg' : 'Account has been registered succesfully',
            }

            return Response (data=response_data, status = status.HTTP_201_CREATED)
        else:
            return Response (data={'status' : '400' , 'msg' : 'Login failed'})
        

#forgot password
class forgotpassword(APIView):
    def post(self,request):
        email=request.data.get('email')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)

            # serializer=forgotpasswordserial(data=request.data)
            # if serializer.is_valid():
            

            current_site=get_current_site(request)
            send_message='Please activate your account'
            massage=render_to_string('account_verification.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
                'cite':current_site.domain,
            })
            mail=user
            sendmail=EmailMessage(send_message,massage,to=[mail])
            sendmail.send()

            response_data = {
                'status': 'success',
                'msg': 'A verification link sent to your registered email address',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            print('Serializer errors are:')
            return Response({'status': 'error'})


#boarding form
class Boardingform(APIView):
    
    def get(self,request):
        boardform=BoardingForm.objects.all()
        serialize=Boardformserial(boardform,many=True)
        return Response({'status':200,'values':serialize.data,'message':'sucess'})
    

    def post(self,request):

        serializer=Boardformserial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status': 400, 'errors': serializer.errors, 'message': 'error'})
        


# board form edit
class BoardingformEdit(RetrieveUpdateDestroyAPIView):
    serializer_class = Boardformserial
    lookup_field = 'id'
    queryset = BoardingForm.objects.all()

# single board user
class Singleboarduserget(RetrieveUpdateDestroyAPIView):
    serializer_class=Userserilizers
    queryset=User.objects.all()

#adminside data update
class UserpassinAdminside(RetrieveUpdateDestroyAPIView):
    serializer_class= Userserilizers
    lookup_field='id'
    queryset=User.objects.all()

# board data get in to the adminside
class Petboardownerlist(ListCreateAPIView):
    serializer_class=Userserilizers
    filter_backends = [SearchFilter]
    search_fields = ['email', 'username', 'roles', 'is_active']

    def get_queryset(self):
        return User.objects.filter(roles='boarduser')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#Taker data get in to the adminside
class Pettakerlist(ListCreateAPIView):
    serializer_class=Userserilizers
    filter_backends=[SearchFilter]
    search_fields=['email', 'username', 'roles', 'is_active']

    def get_queryset(self):
        return User.objects.filter(roles='taker')
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#board profile update

class Updateboardprofile(RetrieveUpdateDestroyAPIView):
    serializer_class=Userserilizers
    lookup_field='id'
    queryset=User.objects.all()


#board redux data passing 
class passingdataRedux(ListAPIView):
    serializer_class=Boardformserial
    def get_queryset(self):
        user_id=self.kwargs['id']
        queryset=BoardingForm.objects.filter(user_id=user_id)
        return queryset
  