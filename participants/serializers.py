from rest_framework import serializers
from participants.models import Participants, PhoneVerify, TestSending, Winners


class ParticipantsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'

class PhoneVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerify
        fields = ('phone', )

class CodeVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerify
        fields = ('phone', 'code')

class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSending
        fields = '__all__'


class WinnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winners
        fields = ('prize', 'first_name', 'patronymic','second_name', 'phone')