from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from .import views
urlpatterns = [
    #tokens
    path('token_obtain_pair/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('users',petboard.as_view()),
    path('activate/<uidb64>/<token> ', views.activate, name='activate'),

    path('googleauth',googlesignup.as_view()),
    path('boardforgotpass',forgotpassword.as_view()),
    path('Boardingform',Boardingform.as_view()),

    

]