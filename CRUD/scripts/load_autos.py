import csv
from autos.models import *

def run():
    file=open('scripts/load_cars.csv')
    print()
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        b,created=make.objects.get_or_create(name=row[3])
        c=auto(nickname=row[0],mileage=row[1],comments=row[2],make=b)
        c.save()
        print(row, "done ")
