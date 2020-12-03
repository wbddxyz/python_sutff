'''
ex33_cycling_event_ca.py
Colin Anderson
17/11/20
J27C76 Software Design and Development
Read a csv file, summarize, and then write some text back to a text file
'''

import csv
from datetime import datetime


time_stamp = datetime.now()
# format  as  10:30 Wednesday 24/06/20
dt_string = time_stamp.strftime('%H:%S %A %d/%m/%y')

def get_total_distance(data):
    total = 0

    for d in data:
        total += d



    return total

def get_average_distance(data):
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
    names = []
    distances = []

    file_in = 'j27c76_20_21.csv'

    with open(file_in) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')  # comma is default - the following is okay
        #csv_reader = csv.reader(csv_file)
        row_count = 0 # required so we can skip over the first row - headers

        for row in csv_reader:  # loop through data
                names.append(row[0] + ' ' )
                distances.append(float(row[2]))


    # summarize data



    


    summary_text = ' '
  


    summary_text += '------------------------------------------\n'
    for x in range(len(names)):
            summary_text += f'{names[x]:<20}    ({distances[x]}) km\n'

    summary_text += '--------------------------------------------\n'


    total_distance = get_total_distance(distances)
    summary_text += f'The total distance cycled was {total_distance:.0f}km\n'
 
    average_distance = get_average_distance(distances)
    summary_text += f'The group average distance cycled was {average_distance:.0f}km\n'
   



    index_max_value = get_index_maximum_value(distances)
    #print(f'The oldest person is {names[index_max_value]} ({ages[index_max_value]})')
    summary_text += f'The student who cycled the most kilometres was {names[index_max_value]} {distances[index_max_value]}km\n'

    


   


    summary_text += '--------------------------------------------\n'

  

    

    # write text back to a new file
    file_out = 'Ex33 Charity Cycling Event Summary CA.txt'
    write_text_to_file(file_out, summary_text)

 



  
    print(summary_text)
   

    

if __name__ == "__main__":
    main()