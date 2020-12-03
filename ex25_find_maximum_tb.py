'''
ex25_find_maximum.py
Tom Bain
27/10/20
J27C76 Software Design and Development
Standard Algorithms - Find Maximum
'''


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


def get_max_index(data):
    max_index = 0
    max_value = data[0]

    for x in range(1, len(data)):
        if data[x] > max_value:
            max_value = data[x]
            max_index = x

    return max_index


def main():
    scores = [63, 43, 82, 69, 99, 4, 89, 142, 60, 76]

    max_value = get_max_value(scores)  # 142
    print(f'The maximum value in the array/list is {max_value}.')

    index_max_value = get_max_index(scores)  # 7
    print(f'The maximum value in the array is at index {index_max_value}.')


if __name__ == "__main__":
    main()
