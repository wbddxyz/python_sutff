
'''
Colin Anderson
ex23_linear_search.py
27/10/20
J27C76 Software Design and development
Standard Algorithms - linear search 



'''
def find_element(data, find):
    for d in data: #loop through our data 
        if d == find:
            return True

    return False

def find_index(data, find):
    for x in range(len(data)): #loop through 0 to end
        if data[x] == find:
            return x # found

    return -1 # not found 



def main():
    data = [63,43,82,69,92,64,89,42,60,42]

    find = int(input('please enter a number to search for:'))

    seek_element = find_element(data, find)


    if seek_element == True:
        print(f"number {find} was found")

    else:
        print(f"number {find} not found")


    #part 2 find element index
    element_index = find_index(data,find)
        
    if element_index >= 0:
        print(f'The element{find} was found at index {element_index}')
    else:
        print(f'The element{find} was not found')

        










if __name__=="__main__":
    main()



