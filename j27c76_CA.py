'''
ex33_cycling_event_ca.py
Colin Anderson
17/11/20
J27C76 Software Design and Development
Read a csv file, summarize, and then write some text back to a text file
'''

import csv



def get_max_value(data):
    '''
    Returns the largest element/value within the data array/list.
    Assumes at least one entry in the data.
    Assumes no duplicates.
    Assumes no sorting
    '''
    max_value = data[0]

    for x in range(1, len(data)):
        if data[x] > max_value:
            max_value = data[x]

    return max_value






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






# code from ex29
def write_text_to_file(file_out, text):
    with open(file_out, 'w') as file_out:  # w = write to file
        file_out.write(text)

def main():
    names = []
    scores = []

    file_in = 'j27c76_20_21.csv'

    with open(file_in) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')  # comma is default - the following is okay
        #csv_reader = csv.reader(csv_file)
        row_count = 0 # required so we can skip over the first row - headers

        for row in csv_reader:  # loop through data
                names.append(row[0] + ' ' )
                scores.append(row[2])


    # summarize data



    


    summary_text = ' '
  


    summary_text += '------------------------------------------\n'
    for x in range(len(names)):
            summary_text += f'{names[x]:<20}    {scores[x]} \n'

    summary_text += '--------------------------------------------\n'


    
 
  

    max_value = get_max_value(scores)  # 142
    print(f'The maximum value in the array/list is {max_value}.')
    


   


    summary_text += '--------------------------------------------\n'

  

    

    # write text back to a new file
    file_out = 'Ex33 Charity Cycling Event Summary CA.txt'
    write_text_to_file(file_out, summary_text)

 



  
    print(summary_text)
   

    

if __name__ == "__main__":
    main()