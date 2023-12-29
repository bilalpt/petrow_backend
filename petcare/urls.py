from django.urls import path
from petcare.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('petcaresignup',Petcare.as_view()),
    path('token_refresh_petcare', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokenobtain_petcare', Generatetoken.as_view()),
    path('TakerAboutpage',TakerAboutView.as_view()),
    path('Takerdetalis',ServiceDescriptionView.as_view()),
    path('TakerDescriptionEdit/<int:id>',ServiceDescriptionEdit.as_view()),
    path('Takerwithpet', Takerwithpet.as_view()),
    path('takeruserinfo/<int:pk>/', TakerUserInfo.as_view()),
    path('TakerprofileEdit/<int:id>',TakerprofileEdit.as_view()),
    path('TakerDetails',Takeridproofclass.as_view()),
    path('TakeridwithformView',TakeridwithformView.as_view()),
    path('TakeraboutEdit/<int:id>',TakeraboutEdit.as_view()),
    path('TakerwithpetEdit/<int:id>',TakerwithpetEdit.as_view()),
    path('TakeridproofEdit/<int:id>',TakeridproofEdit.as_view()),
    # path('TakeraboutgetRedux',TakeraboutgetRedux.as_view()),
    # lilst about page
    path('AboutpageRetrive/<int:id>',AboutpageRetrive.as_view()),
    path('descriptionRetrive/<int:id>',descriptionRetrive.as_view()),
    path('TakerIdRetreve/<int:id>',TakerIdRetreve.as_view()),
    path('Takeridproofallretreave',Takeridproofallretreave.as_view()),


]