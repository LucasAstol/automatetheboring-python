# This is a guess the number game

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a gess')
    guess = int(input())

    if guess < secretNumber:
        print('guess is too low')
    elif guess > secretNumber:
        print('guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job! You guess ed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))    