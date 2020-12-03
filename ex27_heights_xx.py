'''
ex27_heights_xx.py
Name:
Date
J27C76 Software Design and Development

Problem: Find maximum, minimum and calculate average. 
Note: you must make use of function calls

Example of output:

Alice is the tallest at 194 cm
Jamie is the shortest at 145 cm
The average height is  174 cm
'''






def main():
    names = ['Alice', 'Giovanni', 'Henry', 'Jamie', 'Karen',
             'Lloyd', 'Michelle', 'Nicola', 'Roger', 'Sue']

    heights = [194, 181, 161, 145, 175, 183, 178, 177, 165, 185]



    # TODO Find the tallest person
    
def tallest_person(names,heights):
    tallest_height = heights[-1]
    tallest_name = names[-1]
    return tallest_name, tallest_height

print(f'{tallest_name} is the tallest at {tallest_height}')


    # TODO Find the shortest person
def shortest_person():
    shortest_name = names[3]
    shortest_height = heights[3]
    return shortest_height, shortest_name

print(f'{shortest_name} is the shortest at {shortest_height}')


    # TODO Calculate the average height
def average_height(heights):
     average_height = sum(heights) / len(heights)
     return average_height


print(f'The average height is {average_height}')


if __name__ == '__main__':
    main()
