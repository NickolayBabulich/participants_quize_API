import csv
from django.core.management import BaseCommand
from participants.models import Winners, Participants


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.csv') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                participants = Participants.objects.filter(id=row[0]).exists()
                if participants:
                    if not Winners.objects.filter(winner_id=row[0]).exists():
                        winner = Participants.objects.get(id=row[0])
                        obj = Winners.objects.create(
                            winner_id=row[0],
                            first_name=winner.first_name,
                            second_name=winner.second_name[0],
                            patronymic=winner.patronymic,
                            email=winner.email,
                            phone=f'+7 (9**) *** {winner.phone[-4:]}',
                            prize=row[1]
                        )
                    else:
                        pass
                else:
                    pass
