from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token_refresh_petcare', TokenRefreshView.as_view(), name='token_refresh'),
    path('admintoken',Generatetoken.as_view(),name='admintoken'),
    path('Takerrequest',PettakerRequest.as_view()),



]