'''

ex12_equality_and_relational_operators.py
Colin Anderson 
29/09/20
J27C76 Software Design And Development

Conditional Statements
Equality and relational Operators 
    Equality (equal to) ==
    Inequality (not equal to) !=
    Greater than > 
    Greater than or Equal To >=
    Less Than <
    Less Than or Eual To <=


'''







def main():

    # boolean - true or false 
    heating_on = False # 0
    over_16 = True # 1
    print(f'Heating on: {heating_on}')


    # numbers
    operand_1 = 100
    operand_2 = 10

    #Equality (equal to) ==
    print(operand_1 == operand_2) # false
    
    print(f'Over 16 {over_16}')
    
    
    #Inequality (not equal to) !=
    print(operand_1 != operand_2) #true
    
    
    #Greater than >
    print (operand_1 > operand_2) #true 
    
    
    #Greater than or Equal To >=
    print (operand_1 >= operand_2) #true
    
    #Less Than <
    print(operand_1 < operand_2) #false
    
    
    #Less Than or Equal To <=
    print(operand_1 <= operand_2) #false


    #strings
    operand_3 = "Hello"
    operand_4 = "World"
    operand_5 = "Hello"
    print('Strings')
    print(operand_3 == operand_4) #False - not the same

    print(operand_3 != operand_4)

    print(operand_3 == operand_5)

    print(operand_4 != operand_5)

    print() #newline
    # Compund Logical Operators
    #and - true if both sides are true 
    # or - true if one or both sides are true 
    print('compound logical operators')
    print('cat' == 'cat' and 'cat' == 'dog')
    print('cat' == 'cat' and 'cat' == 'cat')

    print('cat' == 'cat' or 'cat' == 'dog')
    print('cat' == 'cat' or 'cat' == 'dog')
    print('cat' == 'dog' or 'cat' == 'cat')
    print('cat' == 'dog' or 'cat' == 'dog')

    print('cat' == 'dog' or 'cat' == 'mouse' or 'cat' == 'cat')





if __name__=='__main__':
    main()