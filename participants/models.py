from django.db import models


class Participants(models.Model):
    '''
    Модель для регистрации участника розыгрыша
    '''

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    district_id = models.IntegerField(default=41)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(blank=True, null=True)
    time_sms_send = models.DateTimeField(blank=True, null=True)
    verify = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.email}'


class PhoneVerify(models.Model):
    '''
    Модель для верификации и подтверждения номера телефона участника розыгрыша
    '''
    phone = models.CharField(max_length=50)
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.phone} - {self.code}'


class TestSending(models.Model):
    '''
    Модель фейкового эндпоинта проверки отправки данных
    '''
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    district_id = models.IntegerField(default=41)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.email}'


class Log(models.Model):
    '''
    Модель для логирования отправки данных
    '''
    status_answer = [
        ('accepted', 'Успешно отправлено'),
        ('rejected', 'Ошибка отправки')
    ]

    user_id = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=25, choices=status_answer)
    server_response = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)


# Add winners
class Winners(models.Model):
    '''
    Модель для учета победителей розыгрыша
    '''
    winner_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    prize = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.winner_id} - {self.first_name} - {self.second_name} - {self.prize}'
