import csv
from django.core.management.base import BaseCommand
from IPL.models import matches, deliveries


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
                list.append(deliveries(match_id=matches.objects.get(id=row['match_id']), inning=row['inning'],
                                       batting_team=row['batting_team'], bowling_team=row['bowling_team'],
                                       over=row['over'], ball=row['ball'],
                                       batsman=row['batsman'],
                                       non_striker=row['non_striker'],
                                       bowler=row['bowler'],
                                       is_super_over=row['is_super_over'],
                                       wide_runs=row['wide_runs'],
                                       bye_runs=row['bye_runs'],
                                       legbye_runs=row['legbye_runs'],
                                       noball_runs=row['noball_runs'],
                                       penalty_runs=row['penalty_runs'],
                                       batsman_runs=row['batsman_runs'],
                                       extra_runs=row['extra_runs'],
                                       total_runs=row['total_runs'],
                                       player_dismissed=row['player_dismissed'],
                                       dismissal_kind=row['dismissal_kind'],
                                       fielder=row['fielder']
                                       )
                            )

                if len(list) > 5000:
                    deliveries.objects.bulk_create(list)
                    list = []

        deliveries.objects.bulk_create(list)
        list = []  # empty the list

        self.stdout.write(
            self.style.SUCCESS(
                f"Dataset Loaded Successfully!"
            )
        )
