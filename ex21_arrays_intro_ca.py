'''
Colin Anderson
13/10/2020
'''



def main():
    scores = [40,60,47,20,100]


    print('scores: ')
    for score in scores:
        print (score)
    print(score)


    print(f'Length/size = {len(scores)}')

    print(f'First Element = {scores[0]}')

    print(f'Last Element = {scores[-1]}')


    scores[0] = 42
    print(f'Element 0 = {scores[0]}')
    print()

    #calculate the average score
    total_scores = 0
    for score in scores:
        total_scores += score
    # average_Score
    average_score = total_scores / len(scores)
    print(f'The average score was {average_score:.0f}')




if __name__ == "__main__":
    main()
    