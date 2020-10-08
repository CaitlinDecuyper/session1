from random import randint

number = randint(1, 100)
guess = int(input('Guess the number (between 1 and 100): '))
while guess != number:
    if guess < number:
        print('Nope, higher...')
    else:
        print('Nope, lower...')
    guess = int(input('Try again: '))
print('Correct! Thank you for playing.')
