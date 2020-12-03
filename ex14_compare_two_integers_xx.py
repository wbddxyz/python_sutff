'''
ex14_compare_two_integers.py
Colin Anderson
29/09/2020
J27C76 Software Design and Development

Examples of output:
    Please enter a whole number: 10
    Please enter another whole number: 20
    The first number (10) is less than the second number (20)

    Please enter a whole number: 20
    Please enter another whole number: 10
    The first number (10) is greater than the second number (20)

    Please enter a whole number: 10
    Please enter another whole number: 10
    The first number (10) is the same as the second number (20)

Note: you must make use of if-elif-else

'''


def main():


    first_number = input("Please enter a whole number ")

    second_number = input("please enter another whole number ")


    if first_number < second_number:
        print(f'the first number : {first_number} is less than the second number :{second_number} ')

    elif first_number > second_number:
          print(f'the first number : {first_number} is greater than the second number :{second_number} ')
    else:  
        4print(f'the first number : {first_number} is the same as the second number : {second_number} ') 






if __name__ == '__main__':
    main()
