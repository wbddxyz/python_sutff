'''
ex08_useful math_functions_CA
Colin Anderson
22/09/20
some useful maths functions 
'''

import math #import math module



def main():
# useful math functions - built in
    x = 10
    y = 100
    z = -10


    #max - returns the larger of a list of numbers 
    max1 = max(x, y, z)
    print('max1 = ', max1)


    #min - returns the smaller of a list of numbers 
    min1 = min(x, y, z)
    print('min1 = ', min1) # -10

    # round - round a number 

    x = 3.1415
    result = round(x, 3) #3.142
    print(result)

    #pow 
    x = 2 
    result = pow(x, 8) #256
    print(result)

    #sqrt - returns the square root for a given number
    #requires math module
    x = 64 
    result = math.sqrt(x) # 8
    print(result)

if __name__ == '__main__':
    main()


