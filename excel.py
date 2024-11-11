import csv

path = 'C:/Users/qpsa7/Desktop/stock/STOCK_DAY_2330_202309.csv'

with open(path, 'r', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        print(row)