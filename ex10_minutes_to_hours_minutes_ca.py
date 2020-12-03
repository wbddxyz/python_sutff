'''
ex10_minutes_to_hours_minutes.py
Colin Anderson
22/09/2020
J27C76 Software Design and Development
An application that will convert a whole number of minutes into hours and minutes.
For example, an input of 141 would be displayed as: 141 minutes = 2 hour(s) and 21 minute(s). 
'''


def main():
    print('Convert a whole number of minutes into hours and minutes')
    number_of_minutes = int(
        input('Please enter a whole number of minutes: '))

    # calculate the number of hours
    hours = int(number_of_minutes / 60) 

    # calculate the remaining number of minutes
    # the  modulo operator, %, is used to retrieve the remainder after a division
    minutes = number_of_minutes % 60


    print(
        f'{number_of_minutes} minutes = {hours} hour(s) and {minutes} minute(s) ')


if __name__ == '__main__':
    main()
