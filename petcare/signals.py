from django.db.models.signals import post_save,post_delete,pre_save
from django.dispatch import receiver
from .models import *
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save,sender=TakerwithIdform)
def adminaccepttaker(sender, instance, created, *args, **kwargs):
    if not created:
        if instance.Takeraccept == True:
            subject = "Taker Approval Status"
            
            message = f"Hi {instance.user.username}, Your Taker Request has approved"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [instance.user.email]

            send_mail(subject,message,from_email,recipient_list)
