

def guess():
    guesses = 1
    while True:
        a = input('Enter number between 1 and 9: ')
        try:
            a = int(a)
        except:
            print('Non-integer was entered. Try again')
            guesses += 1
            continue 
        if not a in range(1,10):
            print('Integer not between 1 and 9. Try again')
            guesses += 1
        elif a > b:
            print('Answer is less than your guess. Try again')
            guesses += 1
        elif a < b:
            print('Answer is greater than your guess. Try again')
            guesses += 1
        else:
            print(f'Congrats! You took {guesses} guesses to win')
            break

from random import randint

b = randint(1, 9)
guess()

