from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields import NullBooleanField
from map.models import Unit, Customer

from openpyxl import load_workbook
import os

class Command(BaseCommand):
    help = "Загрузка Клиентов"
    
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        
    def handle(self, *args, **options):
        wb = load_workbook(filename=options['file']).worksheets[0]
        for row in wb:
            fields = []
            for i in range(0,8):
                fields.append(row[i].value)
            if not fields[1] or  not fields[2]:
                continue               
            else:
                ap = Customer()
                ap.district = fields[0]
                ap.lat = float(fields[1])
                ap.lon = float(fields[2])
                ap.street = fields[4] + " " +  fields[3]
                ap.building = fields[5]
                ap.corpus = fields[6]
                if not fields[7]:
                    
                    ap.unit = None
                else:   
                    unit = Unit.objects.get(n_mt=fields[7])
                    ap.unit = unit
                ap.save()                
                

