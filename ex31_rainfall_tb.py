'''
ex31_rainfall_tb.py
Tom Bain
24/06/20
J27C76 Software Design and Development

'''
import csv
from datetime import datetime


def summarize_rainfall_data(months, rainfall, year):

    summary = f'RBGE {year} Rainfall Report\n'

    summary += ('-' * 50) + '\n'
    for x in range(0, len(months)):
        summary += f'{months[x]}\t{rainfall[x]:.1f} mm\n'
    summary += ('-' * 50) + '\n'

    total = get_total(rainfall)
    summary += f'The total rainfall for the year was: {total:.1f} mm\n'

    avg = get_average(rainfall)
    summary += f'The average monthly rainfall was: {avg:.1f} mm\n'

    # index wettest month - max
    index_max = get_index_maximum(rainfall)
    summary += f'The wettest month was {months[index_max]} with {rainfall[index_max]:.1f} mm of rain\n'

    # index driest month - min
    index_min = get_index_minimum(rainfall)
    summary += f'The driest month was {months[index_min]} with {rainfall[index_min]:.1f} mm of rain\n'

    summary += ('-' * 50) + '\n'
    summary += '\n'

    time_stamp = datetime.now()
    dt_string = time_stamp.strftime('%H:%S %A %d/%m/%y')
    summary += f'Report produced: {dt_string}'

    return summary


def get_index_maximum(data):
    max_value = data[1]
    max_index = 1
    for x in range(2, len(data)):
        if (data[x] > max_value):
            max_value = data[x]
            max_index = x

    return max_index


def get_index_minimum(data):
    min_value = data[1]
    min_index = 1
    for x in range(2, len(data)):
        if (data[x] < min_value):
            min_value = data[x]
            min_index = x

    return min_index


def get_total(data):
    total = 0.0
    for x in data:
        total += x

    return total


def get_average(data):
    total = 0.0
    for x in data:
        total += x
    average = total / len(data)

    return average


def write_text_to_file(file_out, text):
    with open(file_out, 'w') as file_out:  # w = write to file
        file_out.write(text)


def main():

    months=[]
    rainfall = []

    try:
        file_in = 'j27c76_20_21.csv'

        with open(file_in) as csv_file:
            csv_reader = csv.reader(csv_file)
            row_count = 0  

            for row in csv_reader:  
                if row_count == 0:  
                    row_count += 1
                else:
                    months.append(row[0])
                    rainfall.append(row[1])
    except FileNotFoundError:
        print(f'The file {file_in} was not found!')
        input('Press RETURN/ENTER to close this program.')
        exit(0)


    year = 2019
    summary = summarize_rainfall_data(months,rainfall, year)


    file_out = f'Ex31 RBGE {year} Rainfall Summary TB.txt'
    write_text_to_file(file_out, summary)


    print(summary)

    print(f'The above summary was written to {file_out}.')


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
The above summary was written to d:\RBGE 2019 Rainfall Summary.txt.
'''
