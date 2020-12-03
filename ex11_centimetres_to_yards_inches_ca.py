'''
ex11_centimetres_to_yards_inches.py
Colin Anderson
22/09/2020
J27C76 Software Design and Development
An application that will convert a number of centimetres into the equivalent yards, feet and inches.
For example, an input of 127.0 would be displayed as: 127cm = 1Yd, 1ft and 2'
To display a single quotation mark use \'
'''
# constant - avoids the use of magic numbers
CENTIMETRES_TO_INCHES = 0.393701
INCHES_IN_YARD = 36
INCHES_IN_FOOT = 12


def main():
    print('Convert a number of centimetres into yards, feet and inches.')
    number_of_centimeters = float(
        input('Please enter the number of centimetres: '))

    # convert centimetres to inches
    inches = number_of_centimeters / 2.54 #total number of inches 
  

    # calculate the total number of yards
    
    yards = inches / 36

   

    
 
  
    

    # calculate the remaining number of feet
    # calculation the fraction/decimal part of the yards then the whole number of feet
    feet = yards % 3 * 3



    



  
 

    # calculate the remaining number of inches
    
    inches = inches % 12

  
     
    
    
  

    print(
        f'{number_of_centimeters}cm = {int(yards)}Yd, {int(feet)}ft and {int(inches)}\'')


if __name__ == '__main__':
    main()
