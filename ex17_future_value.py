'''
ex17_future_value.py
Colin Anderson
06/10/2020
J27C76 Software Design and Development 
'''



#def calculate_future_value(principal,interest_rate,period):
 #    for x in range(period):
 #       #calculate interest earned for the current year
 #           interest_earned = current_value * interest_rate / 100
        #add interest
 #           future_value = current_value + interest_earned

#            current_value = future_value
#
  #          future_value = calculate_future_value(principal, interest_rate, period)
#
 #           return current_value

years = 5


def calculate_future_value(principal,interest_rate,years):
    for period in range(years):
        future_value = float(principal) * float(interest_rate) ** float(period)



        return future_value



  

   

def main():

    principal = input("please enter the current value")

    interest_rate = input("please enter the interest rate")


    



print  (calculate_future_value(f'{principal},{interest_rate},{years}'))


     
       

      



    
  
    
      



    
    # output 



    


if __name__=='__main__':
    main()
    
  