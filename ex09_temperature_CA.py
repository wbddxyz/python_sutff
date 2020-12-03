'''
ex09_tempreature.py
Colin Anderson  
22/09/2020
J27C76 Software Design and Development
Application that converts from degrees Celsius to degrees Kelvin and Fahrenheit
'''


def main():
    print('Converts from degrees Celsius to degrees Kelvin and Fahrenheit')
    celsius = float(input('Please enter the temperature in degrees Celsius: '))

    # convert Celsius to Kelvin
    kelvin = celsius + 273.15


    # convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32 
   
    
    print(
        f'{celsius:,.2f}°C is equal to {kelvin:,.2f}K and {fahrenheit:,.2f}°F ')  # ° = alt + 0176


if __name__ == '__main__':
    main()
