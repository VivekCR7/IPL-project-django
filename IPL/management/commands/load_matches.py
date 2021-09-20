import csv
from django.core.management.base import BaseCommand
from IPL.models import matches


class Command(BaseCommand):
    help = "Loads data to django model from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]

        list = []
        with open(file_path, "r") as csv_file:
            data = csv.DictReader(csv_file)

            for row in data:
                list.append(matches(id=row['id'], season=row['season'],
                                    city=row['city'], date=row['date'],
                                    team1=row['team1'], team2=row['team2'],
                                    toss_winner=row['toss_winner'],
                                    toss_decision=row['toss_decision'],
                                    result=row['result'], dl_applied=row['dl_applied'], winner=row['winner'],
                                    win_by_runs=row['win_by_runs'],
                                    win_by_wickets=row['win_by_wickets'],
                                    player_of_match=['player_of_match'],
                                    venue=row['venue'], umpire1=row['umpire1'],
                                    umpire2=row['umpire2'], umpire3=row['umpire3'])
                            )

        matches.objects.bulk_create(list)
        list = []  # empty the list

        self.stdout.write(
            self.style.SUCCESS(
                f"Dataset Loaded Successfully!"
            )
        )
