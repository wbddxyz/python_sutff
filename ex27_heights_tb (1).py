'''
ex28_heights_tb.py
Tom Bain
03/11/20
J27C76 Software Design and Development


Problem: Find maximum, minimum and calculate an average. 
Example of output:

Alice is the tallest at 194 cm
Jamie is the shortest at 145 cm
The average height is  174 cm

'''

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
    for height in data:
        total += height

    # now calculate the average 
    average = total / len(data)

    return average



def main():
    names = ['Alice', 'Giovanni', 'Henry', 'Jamie', 'Karen',
             'Lloyd', 'Michelle', 'Nicola', 'Roger', 'Marita']

    heights = [194, 181, 161, 145, 175, 183, 178, 177, 165, 185]

    # Find the tallest person
    index_max_value = get_index_maximum_value(heights)
    print(
        f'{names[index_max_value]} is the tallest at {heights[index_max_value]} cm')

    # Find the shortest person
    index_min_value = get_index_minimum_value(heights)
    print(
        f'{names[index_min_value]} is the shortest at {heights[index_min_value]} cm')
 
    # Calculate the average height
    average = get_average(heights)
    print(f'The average height is  {average:.0f} cm')


if __name__ == '__main__':
    main()
