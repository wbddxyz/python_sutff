'''

ex04_user_input.py
Colin Anderson
15/09/2020
J27C76 Software Design and Development
'''



def main():


    first_number = int(input('please enter the first whole number: '))
    second_number = int(input('please enter the second whole number: '))

    total = first_number + second_number

    print(f'your total is {total}')



if __name__ == '__main__':
    main()