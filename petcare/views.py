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




# Create your views here.

class Generatetoken(TokenObtainPairView):
    userclass=Petcareserilatoken


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
        redirect_url =  'http://localhost:5173/PettakerHome' + '?message=' + message + '?token' + token
    else:
        message = 'Invalid activation link'
        redirect_url = 'http://localhost:5173/CareSignup/' + '?message=' + message
    
    
    return HttpResponseRedirect(redirect_url)



