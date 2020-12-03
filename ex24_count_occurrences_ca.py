'''
ex24
Colin Anderson
27/10/20
'''
def count_occurrences_even(data):
    count = 0
    for x in data:
        if x % 2 == 0:
            count = count + 1
    return count


def count_occurrences_odd(data):
    count = 0
    for x in data:
        if x % 2 == 1:
            count = count + 1



def main():
    numbers = [60, 43, 82, 69, 42, 64, 89, 42, 60, 42]

    count_even = count_occurrences_even(numbers)
    print(f'There are {count_even} even numbers')


    count_odd = count_occurrences_odd(numbers)
    print(f'There are {count_odd} odd numbers')

  

 
    print (len(numbers))





if __name__ == "__main__":
    main()