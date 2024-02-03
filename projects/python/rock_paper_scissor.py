import random


def play_game():
    
    values = ['R','P','S']

    answer = random.choice(values)

    score1 = 0
    score2 = 0

    while True:
        user_input = input('Select R-rock, P-paper,and S-scissor: ').upper()

        if user_input not in values:
            print('Please enter the correct value from the choices.')
            continue



        if user_input == answer:
            print('IT is tie, try again')
            continue

        elif (user_input == 'R' and answer == 'S') or (user_input == 'P' and answer == 'R') or (user_input =='S' and answer == 'P'):
            print('You won')
            score1 +=1
            print(f'score = player:{score1}   computer:{score2}')
            quit = input('If you want to quit press q: ').lower()

            if quit == 'q':
                break
            else:
                continue
            
        else:
            print('You lose:try again')
            score2 +=1

            print(f'score = player:{score1}   computer:{score2}')
            continue


play_game()


 
        

  
