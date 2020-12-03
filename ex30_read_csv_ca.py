'''
ex30_read_csv_tb.py
Colin Anderson
10/11/2020
Read as scv file, summarize, and then write some text/data back to a text file
'''

import csv

def get_youngest(data):
    youngest = data[0]

    for x in range(1, len(data)):
        if data[x] < youngest: # loop through, if current number is greater than max continue looping
            youngest = data[x]
    return youngest


def get_index_minimum_value(data):
  
    min_value = data[0]
    min_index = 0
    for x in range(1, len(data)):
        if (data[x] < min_value):
            min_value = data[x]
            min_index = x

    return min_index




def get_max_index(data):
    max_value = data[0]
    max_index = 0

    for x in range(1, len(data)):
        if data[x] > max_value:
            max_value = data[x]
            max_index = x

    return max_index

def get_oldest(data):
    max_age = data[0]


    for x in range(1, len(data)):
        if data[x] > max_age: # loop through, if current number is greater then max continue looping
            max_age = data[x]
    return max_age



def get_average_age(data):
    average_age = sum(data) / len(data)
    return average_age    


def main():
    names = []
    ages = []

    file_in = "ex30_age_data.csv"

    with open (file_in) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') # comma is default 
        line_count = 0 
        for row in csv_reader:
            if line_count == 0:
                line_count+=1
            else:
                names.append(row[1] + ' ' + row[0])
                ages.append(int(row[2]))


    



        

    max_index = get_max_index(ages)
    print (f'The oldest person is {names[max_index]}  ({ages[max_index]})')
    print()

    


    
    
    index_min_value = get_index_minimum_value(ages)  
    youngest = get_youngest(ages)
    print(f'The youngest person is {names[index_min_value]} ({ages[index_min_value]})')
    print()

    average_age = get_average_age(ages)
    print(f'The average age is {average_age:.0f}')
    print()


    for x in range(1, len(ages)):
        if ages[x] > average_age: # loop through, if current number is greater then max continue looping
            print (f'{names[x]}, {ages[x]}')
    
            


if __name__=="__main__":
    main()