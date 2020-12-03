'''
ex17_multiplication_tables.py
Colin Anderson  
07/10/2020
J27C76 Software Design and Development


'''




def main():
    given_number = int(input('please enter a whole number from 1-12: '))

    for i in range(1,13):
        print(given_number, 'x' , i, '=', given_number*i)

	# TODO


if __name__ == '__main__':
    main()
