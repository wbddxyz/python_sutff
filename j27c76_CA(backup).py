'''
J27c76_CA.py
Colin Anderson
17/11/20
J27C76 Software Design and Development
Read a csv file, summarize, and then write some text back to a text file
'''

import csv










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





def number_of_passes(data):
    passes = 0
    passmark = 120
    for x in range(1,len(data)):
        if (data[x] >= 120):
            passes = passes + 1
    return passes



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


def write_text_to_file(file_out, text):
    with open(file_out, 'w') as file_out:  # w = write to file
        file_out.write(text)

def main():
    names = [] # create new empty lists to store the data 
    scores = []
    surnames = []

    file_in = 'j27c76_20_21.csv'

    with open(file_in) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')  # comma is default - the following is okay
        #csv_reader = csv.reader(csv_file)
        

        for row in csv_reader:  # loop through data
                names.append(row[0] + ' '  ) # add the names of the students to the empty list named names
                surnames.append(row[1])   # add the surnames of the students to the empty list name surnames
                scores.append(int(row[2])) 
 

    # summarize data



    


    summary_text = ' '
  


 

    summary_text += '--------------------------------------------\n'


   
 
    average_score = get_average(scores)
    summary_text += f'The average score for the class was {average_score:.0f}\n'
   

    passes = number_of_passes(scores)
    summary_text += f'The total number of students who passed was {passes} \n' 

    index_max_value = get_index_maximum_value(scores)
   
    summary_text += f'The student with the highest score was {names[index_max_value]}{surnames[index_max_value]} {scores[index_max_value]}\n'

    


   


    summary_text += '--------------------------------------------\n'

  

    

    # write text back to a new file
    file_out = 'j27c76_CA.txt'
    write_text_to_file(file_out, summary_text)

 



  
    print(summary_text)
   

    

if __name__ == "__main__":
    main()