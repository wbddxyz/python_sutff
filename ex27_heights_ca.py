'''
ex27_heights_ca.py
Name:Colin Anderson
04/11/20
J27C76 Software Design and Development

Problem: Find maximum, minimum and calculate average. 
Note: you must make use of function calls

Example of output:

Alice is the tallest at 194 cm
Jamie is the shortest at 145 cm
The average height is  174 cm
'''
names = ['Alice', 'Giovanni', 'Henry', 'Jamie', 'Karen',
             'Lloyd', 'Michelle', 'Nicola', 'Roger', 'Sue']

heights = [194, 181, 161, 145, 175, 183, 178, 177, 165, 185]


def get_max_index(data):
    max_value = data[0]
    max_index = 0

    for x in range(1, len(data)):
        if data[x] > max_value:
            max_value = data[x]
            max_index = x

    return max_index









def get_shortest_height(heights):
    min_value = heights[0]

    for x in range(1, len(heights)):
        if heights[x] < min_value: # loop through, if current number is greater than max continue looping
            min_value = heights[x]
    return min_value



    # TODO Calculate the average height
def get_average_height(heights):
    average_height = sum(heights) / len(heights)
    return average_height

def get_index_minimum_value(data):
  
    min_value = data[0]
    min_index = 0
    for x in range(1, len(data)):
        if (data[x] < min_value):
            min_value = data[x]
            min_index = x

    return min_index



def get_max_value(data):
  
    max_value = data[0]


    for x in range(1, len(data)):
        if data[x] > max_value: 
            max_value = data[x]
    return max_value



def main():


 
    average_height = get_average_height(heights)
    print(f'The average height is {average_height:.0f}')
    print()




    tallest = get_max_index(heights) # 5
    print(f'{names[tallest]} is the tallest at  {heights[tallest]}cm')
    print()




   



    index_min_value = get_index_minimum_value(heights)  
    print(f'The shortest person is {names[index_min_value]} {heights[index_min_value]}cm')
    print()

  


    # TODO Find the tallest person
    





if __name__ == '__main__':
    main()
