'''

ex12_equality_and_relational_operators.py
Colin Anderson 
29/09/20
J27C76 Software Design And Development
flow control - branching



'''


def main():
    score = 42
    high_score = 23

    if score > high_score:
        high_score = score
        print(f'New High-Score: {high_score}')

    heating_on  = False
    temp = 10
    if temp < 21:
        heating_on = True
        print(f'is heating on: {heating_on}')

    # if - else
    age = 17
    min_age = 21
    msg = ' '

    if age>= min_age:
        msg="Age Okay" #true
    else: False
    msg = 'Too Young'


    print(msg)





    temp = 24 # 24 Fine, 30 Hot, 19 Cold
    TOO_HOT = 30
    JUST_FINE = 20

    if temp >= TOO_HOT:
        heating_on = False
        print(f'{temp}° is too hot')
    elif temp < JUST_FINE: #elif = else if
        heating_on = True
        print(f'{temp}° is too cold') # ° = alt+0176
    else:
        print(f'{temp}° is just fine')














if __name__ == '__main__':
    main()