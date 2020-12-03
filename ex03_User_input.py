'''

ex03_user_input.py
Colin Anderson
15/09/2020
J27C76 Software Design and Development
'''

# string is a collection of zero or more characters

def main():
    first_name = input('please enter your first name: ')
    last_name = input('Please enter your last name: ')

    full_name = first_name + ' ' + last_name # Concatenation - join

    print('Welcome '+ full_name + '!')
    print(f'Welcome {full_name}!') #string interpolation

if __name__ == "__main__":
    main()