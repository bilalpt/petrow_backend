from django.db import models
from petboarding.models import *

# Create your models here.


class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_messages')
    reciever=models.ForeignKey(User,on_delete=models.CASCADE,related_name='recieved_messages')
    message =models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            
            return f"{self.sender.first_name} sent to {self.reciever.first_name} at {self.timestamp}"
