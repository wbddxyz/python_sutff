'''
ex15_exam_grade_if.py
Colin Anderson
J27C76 Software Design and Development 
'''

import os

Min_score = 0
Max_score = 100
score = 0

GRADE_A = 90
GRADE_A_STAR = 100
GRADE_B = 80
GRADE_C = 70
GRADE_D = 60
GRADE_E = 50
GRADE_F = 40



def main():
    #ask user for score
    score = int(input(f'please enter a number between {Min_score} and {Max_score}: '))

# check if score is valid - written range

    if score < Min_score or score > Max_score:
        print(f'{score} is out of range')
        print (f'The number must be within the range {Min_score} and {Max_score}: ')
        os.system('cls')
   
        main()

    grade = 'F'
    if score >= GRADE_A_STAR:
        grade = 'A*'
    elif score >= GRADE_A:
        grade = 'A'
    elif score>=GRADE_B:
        grade='B'
    elif score>=GRADE_C:
        grade='C'
    elif score>=GRADE_D:
        grade='D'
    elif score>=GRADE_E:
        grade='E'
    else:
        grade='F'



    print(f'GRADE:{grade}')
    print (f'SCORE: {score}')









if __name__=='__main__':
    main()




