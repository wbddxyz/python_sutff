'''
ex26_find_min_ca.py
Colin Anderson
27/10/20
J27C76 Software Design and Development 
'''





def get_min_value(data):
    min_value = data[0]

    for x in range(1, len(data)):
        if data[x] < min_value: # loop through, if current number is greater than max continue looping
            min_value = data[x]
    return min_value


    




def get_min_index(data):
    min_value = data[0]
    min_index = 0
    for x in range(1,len(data)):
        if data[x] < min_value:
            min_value = data[x]
            min_index = x
    return min_index


def main():
    scores = [33,23,434,456,234,2345,2,43,45]





    min_value = get_min_value(scores)
    print(f'The minimum value in the array is {min_value}')

    index_min_value = get_min_index(scores)
    print(f'The minimum value in the array is at index {index_min_value}')

if __name__=="__main__":
    main()