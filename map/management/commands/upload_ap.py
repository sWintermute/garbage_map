from map.views import unit
from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields import NullBooleanField
from map.models import Unit, Customer

from openpyxl import load_workbook
from decimal import Decimal

class Command(BaseCommand):
    help = "Загрузка Клиентов"
    
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        
    def handle(self, *args, **options):
        wb = load_workbook(filename=options['file']).worksheets[0]
        for row in wb:
            try:
                ap = Customer()
                ap.district = row[2].value  # Район города
                ap.street = row[6].value + " " + row[5].value # Параметр + Улица
                ap.building = int(row[7].value) # Номер дома                
                ap.corpus = row[8].value # Корпус
                if not row[3].value and row[4].value:
                    continue
                else:
                    ap.lat = Decimal(row[3].value)
                    ap.lon = Decimal(row[4].value)
                if not row[10].value:
                    ap.unit = None
                try:
                    cp = Unit.objects.get(n_mt=int(row[10].value))
                    ap.unit = cp
                except:
                    ap.unit = None
                ap.save()
            except:
                continue                


