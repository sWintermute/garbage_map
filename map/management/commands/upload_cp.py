from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields import NullBooleanField
from map.models import Unit, Customer

from openpyxl import load_workbook
from decimal import Decimal


class Command(BaseCommand):
    help = "Загрузка КП"
    
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        
    def handle(self, *args, **options):
        wb = load_workbook(filename=options['file']).worksheets[6]
        for row in wb:
            cp = Unit()
            try:
                cp.n_mt = int(row[0].value)
                cp.address = row[2].value
                cp.lat = Decimal(row[3].value)
                cp.lon = Decimal(row[4].value)
                cp.district = row[8].value
                cp.save()
            except:
                continue                

