'''
ex26_find_minimum_tb.py
Tom Bain
27/10/20
J27C76 Software Design and Development
Standard Algorithms - Find Minimum
'''


def get_minimum_value(data):
    '''
    Returns the smallest element/value within the data array/list.
    Assumes at least one entry in the data.
    Assumes no duplicates.
    Assumes no sorting
    '''
    min_value = data[0]
    for x in range(1, len(data)):
        if (data[x] < min_value):
            min_value = data[x]

    return min_value


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


def main():
    data = [63, 43, 82, 69, 99, 64, 89, 42, 60, 76]

    min_value = get_minimum_value(data)  # 42

    print(f'The minimum value in the array/list is {min_value}.')

    index_min_value = get_index_minimum_value(data)  # 7
    print(f'The minimum value in the array is at index {index_min_value}.')


if __name__ == '__main__':
    main()
