from participants.models import PhoneVerify
import random
import os
from dotenv import load_dotenv

load_dotenv()


def generate_verification_code():
    code = ''.join(random.choices('123456789', k=4))
    return code


def create_verification_code(phone_number, code):
    while True:
        # code = generate_verification_code()
        existing_phone_verify = PhoneVerify.objects.filter(code=code).first()
        if not existing_phone_verify:
            return PhoneVerify.objects.create(phone=phone_number, code=code)
