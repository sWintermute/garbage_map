import sqlite3
import csv

def get_cp_from_csv():
    with open('cp.csv') as f:
        reader = csv.DictReader(f, delimiter="\t")
        result = []
        for row in reader:
            n_mt = row["n_mt"]
            address = row["address"]
            lat = row["lat"]
            lon = row["lon"]
            result.append({"n_mt":n_mt, "lat":lat, "lon":lon, "address":address})
        return result

'''
d = get_cp_from_csv()
for item in d:
    print(item["n_mt"])
'''

'''
from utils import get_cp_from_csv
from map.models import Unit
from map.models import Customer
cp = get_cp_from_csv()
for item in cp:
	bb = Unit.objects.filter(n_mt=item["n_mt"])
	print(len(bb))
	if len(bb)== 0:
		cp = Unit(lat=item["lat"], lon=item["lon"], n_mt=item["n_mt"], address=item["address"])
		cp.save()
	else:	
		continue
'''

def get_ap_from_csv():
    with open('ap.csv') as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            n_mt = row["n_mt"]
            district = row["district"]
            street = row["street"]
            type_street = row["type_street"]
            building = row["building"]
            liter = row["liter"]
            lat = row["lat"]
            lon = row["lon"]
            result.append({"n_mt":n_mt, "district":district, "street":street, "type_street":type_street, "building":building, "liter":liter, "lat":lat, "lon":lon,})
        return result

'''    
d = get_ap_from_csv()
for item in d:
    print(item["n_mt"])
    print(item["district"])
    print(item["street"])
    print(item["type_street"])
    print(item["building"])
    print(item["liter"])
    print("=============================================================")
'''


