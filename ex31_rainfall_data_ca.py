'''
ex30_read_csv_ca.py
Colin Anderson
13/11/20
J27C76 Software Design and Development
Read a csv file, summarize, and then write some text back to a text file
'''

import csv
from datetime import datetime


time_stamp = datetime.now()
# format  as  10:30 Wednesday 24/06/20
dt_string = time_stamp.strftime('%H:%S %A %d/%m/%y')

def get_total_rainfall(data):
    total = sum(data)
    return total

def get_average_rainfall(data):
    average_rainfall = sum(data) / len(data)
    return average_rainfall   



def get_rainfall(month, rainfall):
    for x in range (len(month)):
        print(f'{month[x]}\t{rainfall[x]}mm')
    return month, rainfall

# code from ex25
def get_index_maximum_value(data):
    '''
    Returns the index value of the largest element within the data array/list.
    Assumes at least one element in the data.
    Assumes no duplicates.
    Assumes no sorting.
    '''
    max_value = data[0]
    max_index = 0
    for x in range(1, len(data)):
        if (data[x] > max_value):
            max_value = data[x]
            max_index = x

    return max_index

# code from ex26
def get_index_minimum_value(data):
    '''
    Returns the index value of the smallest element within the data array/list.
    Assumes at least one element in the data.
    Assumes no duplicates.
    Assumes no sorting.
    '''
    min_value = data[0]
    min_index = 0
    for x in range(1, len(data)):
        if (data[x] < min_value):
            min_value = data[x]
            min_index = x

    return min_index


# code from ex22
def get_average(data):
    '''
    Returns the average element value of a  array/list.
    Assumes at least one element in the data.
    '''
    # first calculate the total
    total = 0
    for d in data:
        total += d

    # now calculate the average
    average = total / len(data)

    return average


# code from ex29
def write_text_to_file(file_out, text):
    with open(file_out, 'w') as file_out:  # w = write to file
        file_out.write(text)

def main():
    months = []
    rainfall = []

    file_in = 'ex31_rainfall_data.csv'

    with open(file_in) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')  # comma is default - the following is okay
        #csv_reader = csv.reader(csv_file)
        row_count = 0 # required so we can skip over the first row - headers

        for row in csv_reader:  # loop through data
            if row_count == 0:  # skips row 0 - headers
                row_count += 1
            else:
                months.append(row[0] + ' ')
                rainfall.append(float(row[1]))


    # summarize data



    



    summary_text = 'RBGE 2019 Rainfall Report\n'


    summary_text += '------------------------------------------\n'
    for x in range(len(months)):
            summary_text += f'  {months[x]}       ({rainfall[x]}) mm\n'

    summary_text += '--------------------------------------------\n'


    total_rainfall = round(get_total_rainfall(rainfall))
    summary_text += f'The total rainfall for the year was {total_rainfall}mm\n'
 
    average_rainfall = get_average_rainfall(rainfall)
    summary_text += f'The average monthly rainfall for the year was {average_rainfall:.0f}mm\n'
   



    index_max_value = get_index_maximum_value(rainfall)
    #print(f'The oldest person is {names[index_max_value]} ({ages[index_max_value]})')
    summary_text += f'The wettest month was {months[index_max_value]} {rainfall[index_max_value]}mm\n'

    


    index_min_value = get_index_minimum_value(rainfall)
    #print(f'The youngest person is {names[index_min_value]} ({ages[index_min_value]})')
    summary_text += f'The driest month was {months[index_min_value]} {rainfall[index_min_value]}mm\n'


    summary_text += '--------------------------------------------\n'

  

    

    # write text back to a new file
    file_out = 'Ex31_rainfall_data.txt'
    write_text_to_file(file_out, summary_text)

    print (f'Report produced:{dt_string}')



    print(f'The Above summary data will be  written to file {file_out}.\n')
    print(summary_text)
   

    

if __name__ == "__main__":
    main()
