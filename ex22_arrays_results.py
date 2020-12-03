'''
Colin Anderson
13/10/2020
J27C76 Software design and development
'''



Passmark = 30
students = ['Mickey', 'Bob', 'Chez', 'Donald', 'Eldon', 'Sue']
scores = [29,30,31,10,50,20]

def get_result(score):
    if score >= Passmark:
        return 'Pass'
    else:
        return 'Fail'




def  print_scores_results(students,scores,results):
  
    for x in range (len(students)):
        print(f'{students[x]}\t{scores[x]}\t{results[x]}')



def get_number_of_passes(results):
    number_of_passes = results.count("Pass")
    return number_of_passes




def get_average_score(scores):
    average_score = sum(scores) / len(scores)
    return average_score



def print_passes(students, results):
    print (students[1],students[2],students[4])
    









def print_results(students, results):
    for x in range (len(students)):
        print(f'{students[x]}\t{results[x]}')



def main():
  


    results = []

    for score in scores:
        result = get_result(score) # function call
        results.append(result)

    print('******** TEST SCORES ********** ')
    print_results(students, results)
    print()


    print('******* TEST RESULTS (1) *********')
    print_scores_results(students, scores, results)
    print()


    average_score = get_average_score(scores)
    print(f'The average score is {average_score:.0f}')
    print()

    number_of_passes = get_number_of_passes(results)
    print(f'The number of passes is {number_of_passes}')
    print()

    print('The following students passed: ')
    print_passes(students, results)
    print
  

if __name__ == "__main__":
    main()