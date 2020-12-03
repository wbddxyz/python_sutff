'''
ex07_numbers_operators_tb.py
Tom Bain
17/09/20
basic operators for maths
J27C76 Software Design and Development
'''


def main():
    first_number = 12
    second_number = 5

    # addition
    answer = first_number + second_number
    print(f'{first_number} + {second_number} = {answer}')

    # subtraction
    answer = first_number - second_number
    print(f'{first_number} - {second_number} = {answer}')

    # multiplication
    answer = first_number * second_number
    print(f'{first_number} * {second_number} = {answer}')

    # division
    answer = first_number / second_number
    print(f'{first_number} ÷ {second_number} = {answer:,.1f}')

    # floor division - round towards zero
    #
    print(f'{first_number} // {second_number} = {answer}')

    # modulo - remainder
   #
    print(f'{first_number} %  {second_number} = {answer}')

    # power - squared
    #
    print(f'{second_number}² = {answer}')  # ² = alt+253

    # power - cubed
    #
    print(f'{second_number}³ = {answer}')  # ³ = alt+252

    # power - 4th
    #
    print(f'{second_number}^4 = {answer}')

    # Compound Assignment Operators
    print('Compound Assignment Operators')
    x = 10
    print(x)
    x += 1  # increment x by 1 (11)
    x -= 10  # subtract 10 from x (1)
    x *= 4  # multiply x by 4 (4)
    x /= 2  # divide x by 2 (2)
    print(x)

    #  # Order of Evaluation
    print('Order of Evaluations')
    # BODMAS
    # Brackets
    # Order
    # Division
    # Multiplication
    # Addition
    # Subtraction
    a = (2 + 3) + 5 + 3 * 4 - 1

    print('a =  ', a)

    # Compound Operators

    # Addition - the compound addition operator is  +=
    x = 20
    y = 10



    # Subtraction - the compound subtraction operator is -=
    # If you wish to decrease the value of variable by an amount, we could write


    # Multiplication - the compound multiplication operator is *=


    # Division - the compound division operator is /=


    print(x)



    
if __name__ == '__main__':
    main()
