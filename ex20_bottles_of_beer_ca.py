'''
ex20_bottles_of_beer.py
Colin Anderson
15/10/2020
J27C76 Software Design and Development
The objective of this task is, using a for loop to output the beer song.
 
      The 99 Bottles of Beer Song
 
      99 bottles of beer on the wall, 99 bottles of beer.
      Take one down, pass it around, 98 bottles of beer on the wall.
 
      98 bottles of beer on the wall, 98 bottles of beer.
      Take one down, pass it around, 97 bottles of beer on the wall.
 
        ...
 
      2 bottles of beer on the wall, 2 bottles of beer.
      Take one down, pass it around, 1 bottle of beer on the wall.
 
      1 bottle of beer on the wall, 1 bottle of beer.
      Take one down, pass it around, no more bottles of beer on the wall.
 
      No more bottles of beer on the wall, no more bottles of beer.
      Go to the store and buy some more, 99 bottles of beer on the wall.
      
      STOP
'''




def sing(n):
  if(n==1):
    number_of_bottles = 'bottle'
    bottles_minus_one = 'bottles'
  elif(n == 2):
    number_of_bottles = 'bottles'
    bottles_minus_one = 'bottle'
  else:
    number_of_bottles = 'bottles'
    bottles_minus_one = 'bottles'


  if(n > 0):
    print(str(n) + " " + number_of_bottles + " of beer on the wall, " + str(n) + " " + number_of_bottles + " of beer.")
    print("Take one down and pass it around, " + str(n-1) + " " + bottles_minus_one + " of beer on the wall.")
    print(" ")
  elif(n==0):
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
  else:
      print("error: wheres the booze?")
bottles = 99

while bottles >= 0:
  sing(bottles)
  bottles -= 1
  


def main():

    


  if __name__ == '__main__':
    main()
