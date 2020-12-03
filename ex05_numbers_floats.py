'''
ex05_numbers_floats.py
Colin Anderson
15/09/2020
J27C76 Software Design and Development
'''


def main():
    first_number = float(input('please enter the first number: '))
    second_number = float(input('please enter the second number: '))


    answer = first_number / second_number

    print(f'the answer is{answer:,.3f}')
    print(f'the answer is{answer:,.1f}')
    print(f'the answer is{answer:,.0f}')
    print(f'{first_number} / {second_number} = {int(answer)}')
 


if( __name__ == "__main__"):
    main()