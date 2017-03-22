import csv,os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SMS_2017.settings')
django.setup()

from main.models import StockInfo
file = open(r'stock_data.csv', 'r')
row = csv.reader(file)

def populate():
    count = -1
    for data in row:
        count+=1
        if count>1 and count<20:
            print data
            for j in range (4):
                StockInfo.objects.get_or_create(name=data[0], round_no=j+1, left=0, priceinitial=float(data[8+j]), pricefinal=float(data[8+j]))

if __name__ == '__main__':
    populate()