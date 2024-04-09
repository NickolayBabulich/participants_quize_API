from rest_framework import generics
from rest_framework import status
from participants.models import Participants, PhoneVerify, Winners
from participants.serializers import ParticipantsCreateSerializer, TestCreateSerializer, PhoneVerifySerializer, \
    CodeVerifySerializer, WinnersSerializer
from rest_framework.response import Response
from participants.services import generate_verification_code, create_verification_code
import datetime

from django.db.models.functions import Right
import re


class ParticipantsCreateAPIView(generics.CreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        phone_number = request.data.get('phone')
        verify_object = PhoneVerify.objects.filter(phone=phone_number)
        verify_object.delete()
        for object in self.queryset.filter(phone=phone_number):
            object.verify = datetime.datetime.now()
            object.save()

        return Response({
            'status': status.HTTP_200_OK,
            'created': True,
            'phone_number': phone_number
        })


class PhoneVerifyCreateAPIView(generics.CreateAPIView):
    serializer_class = PhoneVerifySerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone')
        if phone_number is not None:
            try:
                Participants.objects.get(phone=phone_number)
                return Response({'detail': 'Номер уже подтвержден'})

            except Participants.DoesNotExist:
                if PhoneVerify.objects.filter(phone=phone_number):
                    code = generate_verification_code()
                    sending = f'{phone_number}, Код подтверждения: {code}'
                    if sending:
                        object = PhoneVerify.objects.get(phone=phone_number)
                        object.code = code
                        object.save()
                        return Response({
                            'success': True,
                            'sending': sending
                        })
                    else:
                        return Response({
                            'success': False
                        })

                else:
                    code = generate_verification_code()
                    create_verification_code(phone_number, code)
                    sending = f'{phone_number}, Код подтверждения: {code}'
                    if sending:
                        return Response({
                            'success': True,
                            'sending': sending
                        })
                    else:
                        return Response({
                            'success': False
                        })

        else:
            return Response({'detail': 'Номер телефона не предоставлен'}, status=status.HTTP_400_BAD_REQUEST)


class CodeVerifyCreateAPIView(generics.CreateAPIView):
    serializer_class = CodeVerifySerializer

    def create(self, request, *args, **kwargs):
        code = request.data.get('code')
        phone = request.data.get('phone')
        if PhoneVerify.objects.filter(phone=phone).exists() and PhoneVerify.objects.filter(code=code).exists():

            return Response({
                'verify': True,
                'message': 'Номер телефона подтвержден'
            })
        else:
            return Response({
                'verify': False,
                'message': 'Неверный код, попробуйте еще раз'
            })


class TestCreateAPIView(generics.CreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = TestCreateSerializer


class WinnersListAPIView(generics.ListAPIView):
    queryset = Winners.objects.all()
    serializer_class = WinnersSerializer

    def get_queryset(self):
        queryset = Winners.objects.all()
        phone_pattern = re.compile(r'\d{4}$')
        last_four_digits = self.request.GET.get('phone')
        if last_four_digits and phone_pattern.match(last_four_digits):
            queryset = queryset.annotate(
                last_four_digits=Right('phone', 4)
            ).filter(last_four_digits=last_four_digits)
            return queryset
        return queryset
