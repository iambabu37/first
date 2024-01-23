import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Plant  # Update with the correct import statement for your Plant model

class Command(BaseCommand):
    help = 'Import data from Excel sheet into Django model'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']

        try:
            df = pd.read_excel(excel_file_path)

            for index, row in df.iterrows():
                # Assuming YourModel has fields like 'field1', 'field2', etc.
                Plant.objects.create(
                    name=row['Plant'],
                    botanical_name=row['Botanical_name'],
                    family=row["Family"],
                    part_used=row["Part_Used"],
                    active_compound=row["Active_Compounds"],
                    description=row["Properties"],
                    #reference_detail=row["References"]
                )

            self.stdout.write(self.style.SUCCESS('Data import successful'))

        except pd.errors.EmptyDataError as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {e}. The Excel file is empty.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {e}'))