# import necessary module
import random

#Title
print('-------------------------------------')
print('           NUMBERS GAME')
print('-------------------------------------')
print()

# generate random number between 0 and 100
number = random.randint(0,100)

# ask for a name from the user
name = input('What is your name? ')
# ask for a guess from the user
while True:
    try:
        guess = int(input('Guess a number between 0 and 100 '))
    except ValueError:
        # value was not in the numerical format
        print('Please input a numerical value.')
        # loops around to try entering the value again
        continue
    else:
        # value is now in the correct format
        break


# tell the user if they have the correct guess


while guess != number:

    if 0 <= guess < number:
            print('Unlucky, {1}! The number is more than {0}.'.format(guess,name))
            guess = int(input('Guess a number between 0 and 100 '))
    elif 100 >= guess > number:
            print('Unlucky, {1}! The number is less than {0}.'.format(guess,name))
            guess = int(input('Guess a number between 0 and 100 '))
    else:
        print('Sorry {1), {0} isn\'t between 0 and 100.'.format(guess,name))
        guess = int(input('Guess a number between 0 and 100 '))

print('Congratulations, {1}! The number was {0}.'.format(guess,name))