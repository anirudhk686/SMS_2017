import csv,os
from models import StockInfo
file = open(r'stock_data.csv', 'r')
data = csv.reader(file)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

if __name__ == '__main__':
    for i in range(2,29):
        for j in range (4):
            StockInfo.objects.get_or_create(name=data[i][0], round_no=j+1, left=0, priceinitial=data[i][8+j], pricefinal=data[i][8+j])
            StockInfo.save()