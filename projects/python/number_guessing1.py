import random

def play_game():
    answer = random.randint(1,10)
    attempt = 0


    print('Welcome to the number guessing game.')
    print('Please feel free to participte in the game.')


    while True:
        user_input = input('guess a number between 1 and 10: ')

        if not user_input.isdigit():
            print('Invalid input try agin')
            continue
        else:
            user_input = int(user_input)

            if user_input <1 or user_input > 10:
                print("Pleae enter a number within the specified range")
                continue
        

        if user_input == answer:
            print('KUdos , you are right.')
            break
        else:
            if user_input > answer:
                print('TRY again: too high')
            else:
                print('TRY again: too low')

            attempt +=1


play_game()