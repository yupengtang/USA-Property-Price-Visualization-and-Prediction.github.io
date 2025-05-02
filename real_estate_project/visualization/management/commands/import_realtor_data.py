# visualization/management/commands/import_realtor_data.py

import csv
import os
from django.core.management.base import BaseCommand
from visualization.models import Realtor
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'Import realtor_data.csv into the Realtor model'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'realtor_data.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            Realtors = []
            for row in reader:
                if row['prev_sold_date']:
                    try:
                        prev_sold_date = datetime.strptime(row['prev_sold_date'], '%Y-%m-%d').date()
                    except ValueError:
                        prev_sold_date = None
                else:
                    prev_sold_date = None

                realtor = Realtor(
                    brokered_by=row['brokered_by'],
                    status=row['status'],
                    price=float(row['price']) if row['price'] else 0.0,
                    bed=float(row['bed']) if row['bed'] else 0.0,
                    bath=float(row['bath']) if row['bath'] else 0.0,
                    acre_lot=float(row['acre_lot']) if row['acre_lot'] else 0.0,
                    street=row['street'],
                    city=row['city'],
                    state=row['state'],
                    zip_code=row['zip_code'],
                    house_size=float(row['house_size']) if row['house_size'] else 0.0,
                    prev_sold_date=prev_sold_date
                )
                Realtors.append(realtor)
            Realtor.objects.bulk_create(Realtors)
            self.stdout.write(self.style.SUCCESS('Successfully imported realtor data.'))
