from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields import NullBooleanField
from map.models import Unit, Customer

from openpyxl import load_workbook
import os

class Command(BaseCommand):
    help = "Загрузка КП"
    
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        
    def handle(self, *args, **options):
        wb = load_workbook(filename=options['file']).worksheets[0]
        
        for row in wb:
            fields = []
            for i in range(0,5):
                fields.append(row[i].value)
                print(i, row[i].value)
           
            cp = Unit()
            cp.n_mt = fields[0]
            cp.address = fields[1]
     
            cp.lat = float(fields[2])
            cp.lon = float(fields[3])
            cp.district = fields[4]
            cp.save()                
                

