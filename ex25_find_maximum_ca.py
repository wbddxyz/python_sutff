'''
ex25_find_maximum.py
Colin Anderson
27/10/20
'''


def get_max_value(data):
  
    max_value = data[0]


    for x in range(1, len(data)):
        if data[x] > max_value: # loop through, if current number is greater than max continue looping
            max_value = data[x]
    return max_value

def get_max_index(data):
    max_value = data[0]
    max_index = 0

    for x in range(1, len(data)):
        if data[x] > max_value:
            max_value = data[x]
            max_index = x

    return max_index



def main():
    scores = [33,23,434,456,234,2345,2,43,45]


    max_value = get_max_value(scores) #2345
    print (f'The maximum value in the array/list is{max_value}')

    index_max_value = get_max_index(scores) # 5
    print(f'The maximum value in the array is at index {index_max_value}')

if __name__=="__main__":
    main()