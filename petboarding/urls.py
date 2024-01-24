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
    path('boardingformEdit/<int:id>',BoardingformEdit.as_view()),
    path('singleboarduser/<int:pk>/',Singleboarduserget.as_view()),
    path('userpassinadminside/<int:id>',UserpassinAdminside.as_view()),
    path('Petboardownerlist',Petboardownerlist.as_view()),
    path('Pettakerlist',Pettakerlist.as_view()),
    path('Updateboardprofile/<int:id>',Updateboardprofile.as_view()),
    path('passingdataRedux/<int:id>/',passingdataRedux.as_view()),
    path('listtkaerboardingside',listtkaerboardingside.as_view()),
    path('showtakerdetails/<int:id>',showtakerdetails.as_view()),
    path('test',test.as_view()),
    path('GraphUsers/',GraphUsers.as_view()),
    path('Boardinvitation',Boardinvitation.as_view()),

]