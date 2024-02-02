from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# from petboarding.models import User
from petboarding.serilizers import *
from .models import Message

class MessageSerializer(ModelSerializer):
    sender_email=serializers.EmailField(source='sender.email')

    class Meta:
        model=Message
        fields='__all__'