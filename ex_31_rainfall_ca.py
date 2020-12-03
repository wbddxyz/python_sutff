'''
ex31_rainfall_xx.py
Name: Colin Anderson
Date: 10/11/2020
Software Design and Development
Read, manipulate, and then write some text to a text file


'''
#import calendar
import csv
from datetime import datetime


def print_rainfall(month, rainfall):
    for x in range (len(month)):
        print(f'{month[x]}\t{rainfall[x]}')

def get_total_rainfall(data):
    print (sum(data))
    


def main():

    time_stamp = datetime.now()
    # format  as  10:30 Wednesday 24/06/20
    dt_string = time_stamp.strftime('%H:%S %A %d/%m/%y')



with open('ex31_rainfall_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'RBGE 2019 Rainfall Report {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}  {row[1]}mm ')
            line_count += 1
    print(f'Processed {line_count} lines.')

       

if __name__ == '__main__':
    main()

'''
Your code should produce the following:


RBGE 2019 Rainfall Report
--------------------------------------------------
Jan     12.1 mm
Feb     18.4 mm
Mar     80.0 mm
Apr     33.8 mm
May     72.8 mm
Jun     78.8 mm
Jul     100.2 mm
Aug     140.8 mm
Sep     79.4 mm
Oct     106.2 mm
Nov     76.6 mm
Dec     52.4 mm
--------------------------------------------------
The total rainfall for the year was: 851.5 mm
The average monthly rainfall was: 70.1 mm
The wettest month was Aug with 140.8 mm of rain
The driest month was Jan with 12.1 mm of rain
--------------------------------------------------

Report produced: 09:50 Tuesday 03/11/20
The above summary was written to Ex31 RBGE 2019 Rainfall Summary.txt.
'''
