from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('petcaresignup',Petcare.as_view()),
    path('token_refresh_petcare', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokenobtain_petcare', Generatetoken.as_view()),
    path('TakerAboutpage',TakerAboutView.as_view()),
    path('Takerdetalis',ServiceDescriptionView.as_view()),
    path('TakerDescriptionEdit/<int:id>',ServiceDescriptionEdit.as_view()),
    path('Takerwithpet', Takerwithpet.as_view()),


]