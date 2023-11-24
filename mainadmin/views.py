from django.shortcuts import render

from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
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
from petboarding.models import *
from petcare.models import *
from petcare.serilizers import *




# Create your views here.

class Generatetoken(TokenObtainPairView):
    serializer_class=AdmintokenpairSerializers



class PettakerRequest(APIView):
    def get(self,request):
        if TakerwithIdform.user.id:
            boardingusers=TakerwithIdform.objects.all()
            
            serializer=TakerAboutPageserial(boardingusers,many=True)
            return Response({'status':200,'values':serializer.data,'message':'sucess'})

