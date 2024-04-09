from django.core.management import BaseCommand
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=os.getenv('ADMIN_USER')).exists():
            user = User.objects.create(
                username=os.getenv('ADMIN_USER'),
                first_name="Elon",
                last_name="Mask",
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )

            user.set_password(os.getenv('ADMIN_PWD'))
            user.save()
