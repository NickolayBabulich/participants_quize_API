from django.urls import path
from participants.views import ParticipantsCreateAPIView, PhoneVerifyCreateAPIView, TestCreateAPIView, \
    CodeVerifyCreateAPIView, WinnersListAPIView

urlpatterns = [
    path('participants/create/', ParticipantsCreateAPIView.as_view(), name='participants-create'),
    path('participants/phone_verify/', PhoneVerifyCreateAPIView.as_view(), name='phone-verify'),
    path('participants/code/verify/', CodeVerifyCreateAPIView.as_view(), name='code-verify'),
    path('test/create/', TestCreateAPIView.as_view(), name='test-create'),
    path('participants/winners', WinnersListAPIView.as_view(), name='winners')
]
